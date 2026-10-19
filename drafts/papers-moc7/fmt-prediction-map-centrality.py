import json, sys
from collections import deque, defaultdict
d = json.load(open(sys.argv[1]))
nodes = [n["id"] for n in d["nodes"]]
ids = set(nodes)
out = defaultdict(list); inn = defaultdict(list)
for e in d["edges"]:
    assert e["from"] in ids and e["to"] in ids, e
    out[e["from"]].append(e["to"]); inn[e["to"]].append(e["from"])
n = len(nodes)
def bfs(s):
    dist = {s: 0}; q = deque([s])
    while q:
        u = q.popleft()
        for v in out[u]:
            if v not in dist: dist[v] = dist[u] + 1; q.append(v)
    return dist
LRC = {}; HC = {}
for s in nodes:
    dist = bfs(s)
    LRC[s] = (len(dist) - 1) / (n - 1)
    HC[s] = sum(1 / v for k, v in dist.items() if k != s) / (n - 1)
# Brandes betweenness, directed, normalized 1/((n-1)(n-2))
BC = dict.fromkeys(nodes, 0.0)
for s in nodes:
    S = []; P = defaultdict(list); sigma = dict.fromkeys(nodes, 0); sigma[s] = 1
    dist = {s: 0}; q = deque([s])
    while q:
        v = q.popleft(); S.append(v)
        for w in out[v]:
            if w not in dist: dist[w] = dist[v] + 1; q.append(w)
            if dist[w] == dist[v] + 1: sigma[w] += sigma[v]; P[w].append(v)
    delta = dict.fromkeys(nodes, 0.0)
    while S:
        w = S.pop()
        for v in P[w]: delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
        if w != s: BC[w] += delta[w]
for k in BC: BC[k] /= (n - 1) * (n - 2)
# PageRank d=0.85, dangling mass spread uniformly (networkx default)
dmp = 0.85; pr = dict.fromkeys(nodes, 1 / n)
for _ in range(1000):
    dang = sum(pr[u] for u in nodes if not out[u])
    new = {}
    for i in nodes:
        new[i] = (1 - dmp) / n + dmp * (sum(pr[j] / len(out[j]) for j in inn[i]) + dang / n)
    if sum(abs(new[k] - pr[k]) for k in nodes) < 1e-12: pr = new; break
    pr = new
text = {x["id"]: x for x in d["nodes"]}
print("n_nodes", n, "n_edges", len(d["edges"]))
for name, m in [("LRC", LRC), ("HC", HC), ("BC", BC), ("PR", pr)]:
    vals = sorted(m.values())
    med = vals[len(vals)//2]; p90 = vals[int(0.9*(len(vals)-1))]
    print(f"\n== {name}  median={med:.3f} p90={p90:.3f}")
    for k, v in sorted(m.items(), key=lambda kv: -kv[1])[:12]:
        print(f"{k:4s} {v:.3f}  [{text[k]['level']}/{text[k]['kind']}]")
json.dump({k: {"LRC": round(LRC[k],3), "HC": round(HC[k],3), "BC": round(BC[k],4), "PR": round(pr[k],3)} for k in nodes}, open(sys.argv[2], "w"), indent=0)
