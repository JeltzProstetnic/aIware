"""Confidence Database (OSF s46pr) multi-dataset robustness sweep for the FMT
structural orthogonality result: metacognitive efficiency (M-ratio) is decoupled
from first-order performance (d') across many independent perceptual datasets.

Stage 1 (--plan): screen Database_Information.xlsx -> perceptual datasets with
identifiable metacognition (>=4-pt / continuous confidence, enough trials), flag
staircase/adaptive sets from Manipulations+Notes, and map each to its OSF
download URL. Prints the selection plan; downloads nothing.
Stage 2 (--run N): download the top-N (by n_subjects) screened datasets, fit
per-subject d'/meta-d'/M-ratio (Maniscalco-Lau MLE, metad_mle), and report pooled
+ per-dataset M-ratio vs d' orthogonality.
"""
import sys, os, json, csv, urllib.request, urllib.parse, re
import openpyxl

OSF_NODE = "s46pr"
INDEX = "Database_Information.xlsx"
RAWDIR = "cdb_raw"
STAIR_RX = re.compile(r"stair|adaptive|quest|titrat|psi method|2-?down|3-?down|1-?up", re.I)


def osf_get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.api+json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def list_folder(href):
    """Yield (name, kind, download_url) for all items under an OSF folder href, paginated."""
    url = href
    while url:
        d = osf_get(url)
        for x in d["data"]:
            a = x["attributes"]
            dl = x.get("links", {}).get("download")
            yield a["name"], a["kind"], dl, x["relationships"]["files"]["links"]["related"]["href"] if a["kind"] == "folder" else None
        url = d["links"].get("next")


def build_osf_map():
    top = osf_get(f"https://api.osf.io/v2/nodes/{OSF_NODE}/files/osfstorage/?page%5Bsize%5D=100")
    cdb_href = None
    for x in top["data"]:
        if x["attributes"]["name"] == "Confidence Database":
            cdb_href = x["relationships"]["files"]["links"]["related"]["href"]
    assert cdb_href, "Confidence Database folder not found"
    name2url = {}
    for name, kind, dl, sub in list_folder(cdb_href):
        if kind == "file" and name.lower().startswith("data_") and name.lower().endswith(".csv"):
            key = name[len("data_"):-len(".csv")]
            name2url[key] = dl
    return name2url


def screen_index():
    wb = openpyxl.load_workbook(INDEX, data_only=True)
    ws = wb["Database_Information"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = [str(c).strip() for c in rows[0]]
    H = {h: i for i, h in enumerate(hdr)}
    out = []
    for r in rows[1:]:
        if r[H["Name_in_database"]] is None:
            continue
        cat = str(r[H["Category"]] or "")
        conf = str(r[H["Confidence_scale"]] or "")
        manip = str(r[H["Manipulations"]] or "")
        notes = str(r[H["Notes"]] or "")
        try:
            n = int(r[H["Num_subjects"]])
        except Exception:
            n = 0
        try:
            mintr = int(r[H["Min_trials_per_subject"]])
        except Exception:
            mintr = 0
        m = re.match(r"\s*(\d+)", conf)
        conf_pts = int(m.group(1)) if m else (999 if "contin" in conf.lower() else 0)
        stair = bool(STAIR_RX.search(manip + " " + notes))
        out.append(dict(name=r[H["Name_in_database"]], cat=cat, conf=conf, conf_pts=conf_pts,
                        n=n, mintr=mintr, stair=stair, manip=manip[:40], notes=notes[:40]))
    return out


def plan():
    idx = screen_index()
    name2url = build_osf_map()
    perceptual = [d for d in idx if d["cat"].strip().lower() == "perception"]
    elig = [d for d in perceptual if d["conf_pts"] >= 4 and d["n"] >= 10 and d["mintr"] >= 100]
    for d in elig:
        d["url"] = name2url.get(d["name"])
    have = [d for d in elig if d["url"]]
    print(f"index rows={len(idx)} | perceptual={len(perceptual)} | "
          f"eligible(>=4pt,n>=10,trials>=100)={len(elig)} | with OSF csv={len(have)}")
    print(f"OSF data_*.csv files total: {len(name2url)}")
    print(f"\n{'dataset':38s} {'n':>4} {'conf':>10} {'stair':>5}  manip")
    for d in sorted(have, key=lambda x: -x["n"]):
        print(f"{d['name']:38s} {d['n']:>4} {d['conf'][:10]:>10} {str(d['stair']):>5}  {d['manip']}")
    fixed = [d for d in have if not d["stair"]]
    print(f"\nFIXED (non-staircase) perceptual eligible with data: {len(fixed)} "
          f"datasets, total n={sum(d['n'] for d in fixed)} subjects")
    # persist selection
    with open("cdb_selection.json", "w") as f:
        json.dump(sorted(have, key=lambda x: -x["n"]), f, indent=1)
    print("wrote cdb_selection.json")


def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())


def bin_confidence(vals, k=4):
    """Map raw confidence values -> integer 1..K. Native if <=6 distinct levels,
    else per-dataset quantile bins."""
    uniq = sorted(set(vals))
    if len(uniq) <= 6:
        remap = {v: i + 1 for i, v in enumerate(uniq)}
        return [remap[v] for v in vals], len(uniq)
    import numpy as np
    qs = np.quantile(vals, [i / k for i in range(1, k)])
    out = []
    for v in vals:
        b = 1
        for q in qs:
            if v > q:
                b += 1
        out.append(b)
    return out, k


def fit_dataset(path):
    import metad_mle as M
    rows = list(csv.DictReader(open(path, newline="")))
    if not rows:
        return []
    cols = set(rows[0].keys())
    if not ({"Stimulus", "Response", "Confidence", "Subj_idx"} <= cols):
        return []

    # CDB datasets use DIFFERENT binary codings (0/1, 1/2, -1/1, ...). Detect the
    # two distinct Stimulus/Response values and map low->0 (S1), high->1 (S2).
    def distinct(col):
        vs = set()
        for r in rows:
            try:
                vs.add(float(r[col]))
            except (ValueError, TypeError):
                pass
        return sorted(vs)
    sv, rv = distinct("Stimulus"), distinct("Response")
    if len(sv) != 2 or len(rv) != 2:
        return []  # not a clean 2-alternative task
    smap = {sv[0]: 0, sv[1]: 1}
    rmap = {rv[0]: 0, rv[1]: 1}

    subs = {}
    for r in rows:
        try:
            s = float(r["Stimulus"]); rsp = float(r["Response"]); c = float(r["Confidence"])
        except (ValueError, TypeError):
            continue
        if s not in smap or rsp not in rmap:
            continue
        subs.setdefault(r["Subj_idx"], []).append((smap[s], rmap[rsp], c))
    res = []
    for sid, trials in subs.items():
        if len(trials) < 80:
            continue
        confs = [t[2] for t in trials]
        rat, k = bin_confidence(confs)
        stim = [t[0] for t in trials]; resp = [t[1] for t in trials]
        try:
            nR1, nR2 = M.trials2counts(stim, resp, rat, k)
            md, d1, _ = M.fit_meta_d(nR1, nR2)
        except Exception:
            continue
        if not (d1 == d1) or d1 <= 0.1 or md != md:
            continue
        res.append((sid, d1, md, md / d1))
    return res


def run(topn):
    import numpy as np
    sel = json.load(open("cdb_selection.json"))
    fixed = sel[:topn]
    os.makedirs(RAWDIR, exist_ok=True)
    allrows = []
    perds = []
    print(f"Downloading + fitting top {topn} perceptual datasets by n...\n")
    for d in fixed:
        dest = os.path.join(RAWDIR, f"data_{d['name']}.csv")
        try:
            download(d["url"], dest)
            r = fit_dataset(dest)
        except Exception as e:
            print(f"  {d['name']:34s} FAILED ({type(e).__name__})"); continue
        if len(r) < 8:
            print(f"  {d['name']:34s} skipped (only {len(r)} usable subjects)"); continue
        dd = np.array([x[1] for x in r]); mm = np.array([x[3] for x in r])
        dsd = dd.std(ddof=1)
        rr = np.corrcoef(dd, mm)[0, 1] if dsd > 1e-6 else float("nan")
        clamp = "CLAMP" if dsd < 0.25 else ""
        perds.append((d["name"], len(r), dd.mean(), dsd, mm.mean(), rr, clamp))
        for x in r:
            allrows.append((d["name"], x[1], x[2], x[3]))
        print(f"  {d['name']:34s} n={len(r):4d}  d'={dd.mean():.2f}(sd{dsd:.2f})  "
              f"M-ratio={mm.mean():.2f}  r(M,d')={rr:+.2f} {clamp}")

    D = np.array([x[1] for x in allrows]); MD = np.array([x[2] for x in allrows])
    MR = np.array([x[3] for x in allrows])
    ok = np.isfinite(D) & np.isfinite(MR) & (np.abs(MR) < 3)
    fixedr = [p for p in perds if p[6] != "CLAMP"]
    print("\n================ POOLED (all usable subjects) ================")
    print(f"datasets={len(perds)} (fixed={len(fixedr)}, clamped={len(perds)-len(fixedr)}); "
          f"subjects={len(allrows)} (display-trimmed n={ok.sum()})")
    print(f"  d' vs meta-d':  r={np.corrcoef(D[np.isfinite(D)&np.isfinite(MD)], MD[np.isfinite(D)&np.isfinite(MD)])[0,1]:+.3f}")
    print(f"  d' vs M-ratio:  r={np.corrcoef(D[ok], MR[ok])[0,1]:+.3f}  (target: ~0 = orthogonal)")
    perr = [p[5] for p in fixedr if p[5] == p[5]]
    print(f"  per-FIXED-dataset r(M-ratio,d'): median={np.median(perr):+.3f}  "
          f"range=[{min(perr):+.2f},{max(perr):+.2f}]  ({len(perr)} datasets)")
    json.dump({"perds": perds, "pooled_n": len(allrows)}, open("cdb_results.json", "w"), indent=1)
    np.save("cdb_pooled.npy", np.array([(x[1], x[2], x[3]) for x in allrows]))
    print("wrote cdb_results.json + cdb_pooled.npy")


if __name__ == "__main__":
    if "--plan" in sys.argv:
        plan()
    elif "--run" in sys.argv:
        run(int(sys.argv[sys.argv.index("--run") + 1]))
    else:
        print("usage: cdb_sweep.py --plan | --run N")
