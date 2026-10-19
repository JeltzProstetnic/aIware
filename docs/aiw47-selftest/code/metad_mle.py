"""Single-subject meta-d' MLE estimator (Maniscalco & Lau, 2012).

Pure Python stdlib only (no numpy/scipy/metadpy available in this sandbox:
pip is blocked). Implements:
  - type-1 d' and criterion from a 2x2 SDT table
  - meta-d' via maximum-likelihood fit of the response-conditional type-2
    SDT model to the observed confidence-rating counts (nR_S1, nR_S2),
    following the equal-variance SDT formulation of Maniscalco & Lau (2012),
    "A signal detection theoretic approach for estimating metacognitive
    sensitivity from confidence ratings", Consciousness and Cognition.
  - M-ratio = meta-d'/d' and M-diff = meta-d' - d'.

The optimiser is a from-scratch Nelder-Mead (downhill simplex). The normal
CDF/PDF come from math.erf.

Validation against published worked values is in test_metad_mle.py.
"""
import math

SQRT2 = math.sqrt(2.0)


def _softplus(x):
    """Overflow-safe log(1 + exp(x))."""
    if x > 0:
        return x + math.log1p(math.exp(-x))
    return math.log1p(math.exp(x))


def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / SQRT2))


def norm_ppf(p):
    """Inverse normal CDF (Acklam's rational approximation, |err|<1.15e-9)."""
    if p <= 0.0:
        return -math.inf
    if p >= 1.0:
        return math.inf
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / \
           (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


def trials2counts(stimulus, response, rating, n_ratings):
    """Build nR_S1, nR_S2 response-count vectors.

    stimulus, response in {0,1} (0=S1, 1=S2). rating in 1..n_ratings.
    nR_S1[i]: for S1 trials, counts ordered from
      'responded S1 with highest confidence' ... 'responded S2 with highest
      confidence' (length 2*n_ratings). Same ordering for nR_S2.
    (Maniscalco & Lau convention.)
    """
    nR_S1 = [0] * (2 * n_ratings)
    nR_S2 = [0] * (2 * n_ratings)
    for s, r, c in zip(stimulus, response, rating):
        c = int(c)
        if r == 0:  # responded S1
            idx = n_ratings - c          # high-conf S1 -> index 0
        else:       # responded S2
            idx = n_ratings + (c - 1)    # low-conf S2 ... high-conf S2
        if s == 0:
            nR_S1[idx] += 1
        else:
            nR_S2[idx] += 1
    return nR_S1, nR_S2


def _pad(nR_S1, nR_S2):
    """Add 1/(2*nRatings) to each cell (standard padding for empty cells)."""
    n_ratings = len(nR_S1) // 2
    add = 1.0 / (2 * n_ratings)
    return ([x + add for x in nR_S1], [x + add for x in nR_S2])


def type1_dprime(nR_S1, nR_S2):
    """Type-1 d' and criterion c from the collapsed 2x2 table (with padding)."""
    nr1, nr2 = _pad(nR_S1, nR_S2)
    n_ratings = len(nr1) // 2
    # responded S2 = second half of each vector
    S1_resp_S2 = sum(nr1[n_ratings:])   # false alarms (S1 trials, "S2" resp)
    S1_resp_S1 = sum(nr1[:n_ratings])
    S2_resp_S2 = sum(nr2[n_ratings:])   # hits (S2 trials, "S2" resp)
    S2_resp_S1 = sum(nr2[:n_ratings])
    H = S2_resp_S2 / (S2_resp_S2 + S2_resp_S1)
    FA = S1_resp_S2 / (S1_resp_S2 + S1_resp_S1)
    d1 = norm_ppf(H) - norm_ppf(FA)
    c1 = -0.5 * (norm_ppf(H) + norm_ppf(FA))
    return d1, c1


def _nelder_mead(f, x0, step=0.1, tol=1e-8, max_iter=4000):
    """Minimise f over R^n. Plain downhill simplex."""
    n = len(x0)
    alpha, gamma, rho, sigma = 1.0, 2.0, 0.5, 0.5
    simplex = [list(x0)]
    for i in range(n):
        x = list(x0)
        x[i] += step if x[i] == 0 else step * abs(x[i])
        simplex.append(x)
    fvals = [f(x) for x in simplex]
    for _ in range(max_iter):
        order = sorted(range(n + 1), key=lambda i: fvals[i])
        simplex = [simplex[i] for i in order]
        fvals = [fvals[i] for i in order]
        if abs(fvals[-1] - fvals[0]) < tol:
            break
        centroid = [sum(simplex[i][j] for i in range(n)) / n for j in range(n)]
        # reflection
        xr = [centroid[j] + alpha * (centroid[j] - simplex[-1][j]) for j in range(n)]
        fr = f(xr)
        if fvals[0] <= fr < fvals[-2]:
            simplex[-1], fvals[-1] = xr, fr
            continue
        if fr < fvals[0]:
            xe = [centroid[j] + gamma * (xr[j] - centroid[j]) for j in range(n)]
            fe = f(xe)
            if fe < fr:
                simplex[-1], fvals[-1] = xe, fe
            else:
                simplex[-1], fvals[-1] = xr, fr
            continue
        xc = [centroid[j] + rho * (simplex[-1][j] - centroid[j]) for j in range(n)]
        fc = f(xc)
        if fc < fvals[-1]:
            simplex[-1], fvals[-1] = xc, fc
            continue
        for i in range(1, n + 1):
            simplex[i] = [simplex[0][j] + sigma * (simplex[i][j] - simplex[0][j])
                          for j in range(n)]
            fvals[i] = f(simplex[i])
    order = sorted(range(n + 1), key=lambda i: fvals[i])
    return simplex[order[0]], fvals[order[0]]


def fit_meta_d(nR_S1, nR_S2):
    """Estimate meta-d' (Maniscalco & Lau 2012, equal-variance SDT).

    Free params: meta-d', and (nRatings-1) type-2 criteria for each response.
    The type-1 criterion is fixed from the data (c1), and type-2 criteria are
    parameterised as offsets that keep the ordering. We fit meta-d' plus
    2*(nRatings-1) type-2 criteria by ML on the rating counts.
    """
    nr1, nr2 = _pad(nR_S1, nR_S2)
    n_ratings = len(nr1) // 2
    d1, c1 = type1_dprime(nR_S1, nR_S2)
    # observed counts per rating bin
    obs = nr1 + nr2  # length 4*nRatings

    # type-2 criteria: (nRatings-1) for "responded S1" side (left of c1),
    # (nRatings-1) for "responded S2" side (right of c1).
    n_t2 = n_ratings - 1

    def negloglik(params):
        md = params[0]
        # enforce ordered criteria via cumulative softplus offsets
        # S1-side criteria: below c1, decreasing confidence toward c1
        cS1 = []
        base = c1
        for k in range(n_t2):
            base -= _softplus(params[1 + k])  # strictly < previous
            cS1.append(base)
        cS1 = cS1[::-1]  # ascending toward c1
        cS2 = []
        base = c1
        for k in range(n_t2):
            base += _softplus(params[1 + n_t2 + k])
            cS2.append(base)
        # full set of boundaries for S1-response region: [-inf, cS1..., c1]
        # and S2-response region: [c1, cS2..., +inf]
        S1mu = -md / 2.0
        S2mu = md / 2.0
        # boundaries left of c1 (responded "S1"): from most-confident-S1 to c1
        leftb = [-math.inf] + cS1 + [c1]
        rightb = [c1] + cS2 + [math.inf]

        # probabilities of each rating bin under S1 and S2 distributions
        def binprobs(mu):
            # responded S1 bins: between consecutive leftb (high conf -> low)
            ps1 = []
            for i in range(n_ratings):
                lo, hi = leftb[i], leftb[i + 1]
                ps1.append(norm_cdf(hi - mu) - norm_cdf(lo - mu))
            # responded S2 bins: between consecutive rightb (low conf -> high)
            ps2 = []
            for i in range(n_ratings):
                lo, hi = rightb[i], rightb[i + 1]
                ps2.append(norm_cdf(hi - mu) - norm_cdf(lo - mu))
            return ps1 + ps2  # length 2*nRatings

        pS1 = binprobs(S1mu)   # for S1 stimulus trials
        pS2 = binprobs(S2mu)   # for S2 stimulus trials
        probs = pS1 + pS2
        ll = 0.0
        for o, p in zip(obs, probs):
            p = min(max(p, 1e-12), 1.0)
            ll += o * math.log(p)
        return -ll

    x0 = [d1] + [0.0] * (2 * n_t2)
    best, _ = _nelder_mead(negloglik, x0, step=0.2, max_iter=6000)
    # second restart from a slightly different seed for robustness
    best2, f2 = _nelder_mead(negloglik, [max(0.1, d1 * 0.8)] + [0.1] * (2 * n_t2),
                             step=0.2, max_iter=6000)
    f1 = negloglik(best)
    meta_d = best[0] if f1 <= f2 else best2[0]
    return meta_d, d1, c1
