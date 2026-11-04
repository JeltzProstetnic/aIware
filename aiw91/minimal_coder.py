"""AIW-91 Increment 1 — minimal critical recursive coder (mechanism proof).

One recursive 3-layer coder realised as a stochastic binary spiking net:
    input drive -> CRITICAL MIDDLE (two hemispheres, branching sigma ~ G) -> readout action a(t)
    a(t) folded back INTERNALLY into the next input (closure / efference).

Criticality machinery is the AIW-90 one in discrete spikes: recurrent matrix W normalised to
spectral radius 1, gain G is the knob, branching sigma ~ G (critical at G=1). At criticality the
middle layer's state carries a decodable world-code (EWM) and a decodable self-code (ESM = the
fed-back action), with the self nested in the world (O_ESM subset of S_EWM). The whole point:
this only holds AT criticality and WITH the loop closed.

Pure numpy. Seedable. See ROADMAP.md / ../docs/aiw91-minimal-critical-substrate.md.
"""
from __future__ import annotations
import numpy as np


# ----------------------------------------------------------------------------- world
class World:
    """Minimal world: a slow continuous latent with its own dynamics (AR(1)).

    Human-like-minimal = a continuous variable to be tracked (heading/quantity-like),
    not a classification toy. z(t) is what the EWM must come to represent.
    """
    def __init__(self, rho=0.92, sigma=0.35, seed=0):
        self.rho, self.sigma = rho, sigma
        self.rng = np.random.default_rng(seed)
        self.z = 0.0

    def step(self):
        self.z = self.rho * self.z + self.sigma * self.rng.standard_normal()
        return self.z


# ----------------------------------------------------------------- recursive coder
class RecursiveCriticalCoder:
    """Two-hemisphere probabilistic BRANCHING network (Galton-Watson realised in spikes).

    A spike in neuron j activates each downstream neuron i with prob w_ij. The adjacency is
    column-normalised (sum_i w_ij = 1), so a spike has G expected descendants => branching
    sigma = G, CRITICAL at G=1 (sub-critical activity dies, super-critical explodes; at the
    edge: scale-free avalanches). Perturbation growth rate lambda = log(sigma) = log G — a clean,
    monotone criticality knob, unlike the saturating E/I-sigmoid net.

    p_rec_i  = G * sum_j w_ij s_j(t-1)                          (recurrent activation prob)
    p_drv_i  = b_world*sig(w_world_i z) + closure*b_self*sig(w_self_i a(t-1))   (world+self drive)
    P_i      = 1 - (1-p_spont)(1-p_rec_i)(1-p_drv_i)            (spike prob)
    s_i(t)   ~ Bernoulli(P_i)
    r_i(t)   = alpha r_i(t-1) + (1-alpha) s_i(t)                (leaky rate -> decode/readout)
    a(t)     = tanh(w_out . r(t)) ; closure folds a(t-1) into next input (internal efference).

    Two hemispheres: out-edges stay same-hemisphere w.p. ~ (1-c_inter); 'simple cortex, two halves'.
    """
    def __init__(self, N=1000, K=20, G=1.0, c_inter=0.15, p_spont=0.0003, drive_slope=2.5,
                 alpha=0.6, b_world=0.15, b_self=0.15, w_out_scale=4.0, closure=True,
                 refractory=True, seed=0):
        assert N % 2 == 0
        self.N, self.G, self.closure, self.refractory = N, G, closure, refractory
        self.p_spont, self.drive_slope, self.alpha = p_spont, drive_slope, alpha
        self.b_world, self.b_self = b_world, b_self
        rng = np.random.default_rng(seed)
        self.rng = rng
        half = N // 2

        # sparse directed non-negative adjacency, mostly within hemisphere
        rows, cols, vals = [], [], []
        for j in range(N):                                  # j = presynaptic (column)
            same_pool = np.arange(0, half) if j < half else np.arange(half, N)
            other_pool = np.arange(half, N) if j < half else np.arange(0, half)
            tgt = []
            for _ in range(K):
                if rng.random() < c_inter:
                    tgt.append(rng.choice(other_pool))
                else:
                    tgt.append(rng.choice(same_pool))
            tgt = np.array(tgt)
            w = rng.random(K)
            w = w / w.sum()                                 # COLUMN-normalise: descendants of j sum to 1
            for i, wv in zip(tgt, w):
                rows.append(i); cols.append(j); vals.append(wv)
        from scipy.sparse import csr_matrix
        self.W = csr_matrix((vals, (rows, cols)), shape=(N, N))

        self.w_world = rng.standard_normal(N)
        self.w_self = rng.standard_normal(N)
        self.w_out = w_out_scale * rng.standard_normal(N) / np.sqrt(N)

        self.s = np.zeros(N)
        self.r = np.zeros(N)
        self.a_prev = 0.0

    @staticmethod
    def _sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    def step(self, z, noise_unused=None, unif=None):
        """One update. Pass `unif` (N-vector in [0,1)) to drive two copies with SHARED spike
        draws (the perturbation/Lyapunov measure needs it); else draw internally."""
        p_rec = self.G * (self.W @ self.s)
        p_drv = self.b_world * self._sigmoid(self.drive_slope * self.w_world * z)
        if self.closure:
            p_drv = p_drv + self.b_self * self._sigmoid(self.drive_slope * self.w_self * self.a_prev)
        P = 1.0 - (1.0 - self.p_spont) * (1.0 - np.clip(p_rec, 0, 1)) * (1.0 - np.clip(p_drv, 0, 1))
        if self.refractory:
            P = P * (1.0 - self.s)            # neurons that spiked last step are silenced (refractory)
        u = self.rng.random(self.N) if unif is None else unif
        self.s = (u < P).astype(float)
        self.r = self.alpha * self.r + (1.0 - self.alpha) * self.s
        a = np.tanh(self.w_out @ self.r)
        self.a_prev = a
        return a

    def run(self, world: World, T=4000, burn=400):
        """Drive the coder with the world for T+burn steps; return logged arrays."""
        Z, A, R, S, Apre = [], [], [], [], []
        for t in range(T + burn):
            z = world.step()
            a_pre = self.a_prev           # self signal injected this step (before update)
            a = self.step(z)
            if t >= burn:
                Z.append(z); A.append(a); R.append(self.r.copy())
                S.append(self.s.copy()); Apre.append(a_pre)
        return dict(z=np.array(Z), a=np.array(A), R=np.array(R),
                    S=np.array(S), a_prev=np.array(Apre))


# ---------------------------------------------------- critical reservoir variant
class ReservoirCoder:
    """Two-hemisphere rate-reservoir variant — the tractable substrate where the *dynamical*
    edge of chaos (spectral radius G ~ 1) genuinely MAXIMISES memory/recursive computation
    (Bertschinger & Natschlaeger 2004). Used to demonstrate the closure-AT-criticality principle
    cleanly; the spiking branching net (RecursiveCriticalCoder) is the target substrate to port to.

    x(t) = (1-leak) x(t-1) + leak * tanh( G * W x(t-1) + b_world*win_w*z + closure*b_self*win_s*a(t-1) )
    a(t) = tanh(w_out . x(t)) ; a(t-1) folded back internally (closure). Edge of chaos at G~1.
    """
    def __init__(self, N=600, K=30, G=1.0, c_inter=0.2, leak=0.5, b_world=0.5, b_self=0.5,
                 w_out_scale=1.0, closure=True, seed=0):
        assert N % 2 == 0
        self.N, self.G, self.leak, self.closure = N, G, leak, closure
        self.b_world, self.b_self = b_world, b_self
        rng = np.random.default_rng(seed); self.rng = rng
        half = N // 2
        W = np.zeros((N, N))
        for i in range(N):
            pre = rng.choice(N, size=K, replace=False)
            w = rng.standard_normal(K)
            same = (pre < half) == (i < half)
            W[i, pre] = w * np.where(same, 1.0, c_inter)
        self.W = W / np.abs(np.linalg.eigvals(W)).max()      # spectral radius 1 -> G is the knob
        self.win_w = rng.standard_normal(N)
        self.win_s = rng.standard_normal(N)
        self.w_out = w_out_scale * rng.standard_normal(N) / np.sqrt(N)
        self.x = np.zeros(N); self.a_prev = 0.0

    def step(self, z, _noise=None, perturb=None):
        drive = self.b_world * self.win_w * z
        if self.closure:
            drive = drive + self.b_self * self.win_s * self.a_prev
        pre = self.G * (self.W @ self.x) + drive
        self.x = (1 - self.leak) * self.x + self.leak * np.tanh(pre)
        if perturb is not None:
            self.x = self.x + perturb; perturb = None
        a = np.tanh(self.w_out @ self.x)
        self.a_prev = a
        return a

    def run(self, world: World, T=3000, burn=400):
        Z, A, R, Apre = [], [], [], []
        for t in range(T + burn):
            z = world.step(); a_pre = self.a_prev; a = self.step(z)
            if t >= burn:
                Z.append(z); A.append(a); R.append(self.x.copy()); Apre.append(a_pre)
        return dict(z=np.array(Z), a=np.array(A), R=np.array(R), a_prev=np.array(Apre))


def reservoir_lyapunov(kw, T=400, burn=200, eps=1e-6, world_seed=0):
    """Edge-of-chaos for the rate reservoir: shared input, infinitesimal state perturbation,
    mean log-divergence rate. lambda<0 ordered, >0 chaotic, ~0 critical (G~1)."""
    c1 = ReservoirCoder(**kw); c2 = ReservoirCoder(**kw)
    w = World(seed=world_seed); zs = [w.step() for _ in range(T + burn)]
    for t in range(burn):
        c1.step(zs[t]); c2.step(zs[t])
    c2.x = c1.x.copy(); c2.a_prev = c1.a_prev
    d0 = eps * np.sqrt(c1.N); c2.x = c2.x + eps
    logs = []; d_prev = np.linalg.norm(c1.x - c2.x) + 1e-30
    for t in range(burn, T + burn):
        c1.step(zs[t]); c2.step(zs[t])
        d = np.linalg.norm(c1.x - c2.x)
        if d > 0: logs.append(np.log(d / d_prev))
        # renormalise to keep in the tangent (linear) regime
        if d > 1e-3:
            f = d0 / d; c2.x = c1.x + (c2.x - c1.x) * f; d = d0
        d_prev = d + 1e-30
    return float(np.mean(logs)) if logs else float("nan")


# --------------------------------------------------------------------- measures
def ridge_decode(R, y, train_frac=0.7, lam=1.0):
    """Ridge linear decode of scalar target y from state R; return held-out R^2 and weights."""
    R = np.asarray(R); y = np.asarray(y).ravel()
    n = len(y); ntr = int(n * train_frac)
    Xtr, Xte = R[:ntr], R[ntr:]
    ytr, yte = y[:ntr], y[ntr:]
    mu = Xtr.mean(0); sd = Xtr.std(0) + 1e-8
    Xtr = (Xtr - mu) / sd; Xte = (Xte - mu) / sd
    ym = ytr.mean()
    A = Xtr.T @ Xtr + lam * np.eye(Xtr.shape[1])
    w = np.linalg.solve(A, Xtr.T @ (ytr - ym))
    pred = Xte @ w + ym
    ss_res = np.sum((yte - pred) ** 2)
    ss_tot = np.sum((yte - yte.mean()) ** 2) + 1e-12
    return 1.0 - ss_res / ss_tot, w


def branching_sigma(S):
    """Branching ratio estimate sigma ~ slope of A(t+1) on A(t) (population spike count)."""
    A = np.asarray(S).sum(1).astype(float)
    a0, a1 = A[:-1], A[1:]
    a0c = a0 - a0.mean()
    denom = np.sum(a0c * a0c)
    if denom <= 0:
        return float("nan")
    return float(np.sum(a0c * (a1 - a1.mean())) / denom)


def mean_activity(S):
    return float(np.asarray(S).mean())


def subspace_alignment(w_world, w_self):
    """|cosine| between world- and self-decoder directions in state space.
    High => self is coded along the SAME directions as the world (O_ESM nested in S_EWM);
    ~0 => self lives in an orthogonal subspace (separate, not nested)."""
    a = w_world / (np.linalg.norm(w_world) + 1e-12)
    b = w_self / (np.linalg.norm(w_self) + 1e-12)
    return float(abs(a @ b))


def lyapunov(coder_kwargs, T=500, burn=120, eps_flips=8, world_seed=0, draw_seed=99):
    """Drive-robust edge-of-chaos measure: run two identical copies with SHARED world+noise+
    threshold draws, perturb one copy's state, track state-distance growth. Returns the mean
    log-divergence rate lambda. lambda<0 ordered (sub-critical), >0|chaotic (super), ~0 critical.

    Input cancels (identical streams) so only the intrinsic recurrent dynamics drive divergence.
    """
    c1 = RecursiveCriticalCoder(**coder_kwargs)
    c2 = RecursiveCriticalCoder(**coder_kwargs)         # same seed -> identical W, projections
    N = c1.N
    w = World(seed=world_seed)
    drng = np.random.default_rng(draw_seed)
    # shared draws
    zs = [w.step() for _ in range(T + burn)]
    noises = drng.standard_normal((T + burn, N))
    unifs = drng.random((T + burn, N))

    for t in range(burn):                                # settle both identically
        c1.step(zs[t], noises[t], unifs[t]); c2.step(zs[t], noises[t], unifs[t])
    # perturb copy 2: flip a few spikes
    c2.s = c1.s.copy()
    flip = drng.choice(N, size=eps_flips, replace=False)
    c2.s[flip] = 1.0 - c2.s[flip]
    c2.r = c1.r.copy(); c2.a_prev = c1.a_prev

    logr = []
    d_prev = np.linalg.norm(c1.s - c2.s) + 1e-12
    for t in range(burn, T + burn):
        c1.step(zs[t], noises[t], unifs[t]); c2.step(zs[t], noises[t], unifs[t])
        d = np.linalg.norm(c1.s - c2.s)
        if d > 0:
            logr.append(np.log(d / d_prev))
        d_prev = d + 1e-12
        if d_prev > np.sqrt(N):                          # saturated; stop the linear regime
            break
    return float(np.mean(logr)) if logr else float("-inf")
