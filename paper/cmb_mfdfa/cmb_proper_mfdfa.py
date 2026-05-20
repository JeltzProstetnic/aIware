#!/usr/bin/env python3
"""
Proper spherical MFDFA analysis of Planck 2018 SMICA CMB map.

Needlet-based multifractal detrended fluctuation analysis:
- Decomposes map into needlet bands (respects spherical geometry)
- Runs MFDFA on needlet coefficient maps
- Compares against 500 Gaussian simulations at full Nside=2048
- Applies consistent masking throughout

Output: tmp/cmb-data/proper_mfdfa_results.npz + 6 publication-quality figures
Runtime: ~2-3 hours on 48GB RAM WSL (8 workers)

Memory profile per worker: ~3.5GB (map + ALM + 7 needlet bands).
8 workers = ~28GB + 4GB main = ~32GB peak. Safe on 48GB WSL.
Previous config crashed WSL2 when WSL had only 32GB (default 50% of host).
"""

import multiprocessing
multiprocessing.set_start_method('spawn', force=True)

import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from multiprocessing import Pool, cpu_count
import gc
import time
import os
import sys

OUT_DIR = 'tmp/cmb-data'
NSIDE_DATA = 2048
N_SIMS = 500
N_WORKERS = 8  # 8 × 3.5GB = 28GB workers + 4GB main = ~32GB peak (safe on 48GB WSL)
Q_VALUES = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Needlet band definitions (ℓ ranges for band-pass filtering)
# Each band covers a range of multipoles — logarithmically spaced
NEEDLET_BANDS = [
    (2, 10),      # Band 0: largest scales (anomalies live here)
    (10, 30),     # Band 1: large scales
    (30, 100),    # Band 2: intermediate
    (100, 300),   # Band 3: first acoustic peak region
    (300, 800),   # Band 4: acoustic peaks
    (800, 1500),  # Band 5: damping tail
    (1500, 2500), # Band 6: small scales
]


def needlet_filter(alm, lmax, ell_min, ell_max):
    """Apply a smooth band-pass filter in harmonic space (cosine taper)."""
    # Cosine taper for smooth transitions (avoid ringing)
    taper_width = max(5, (ell_max - ell_min) // 10)
    
    fl = np.zeros(lmax + 1)
    for ell in range(lmax + 1):
        if ell < ell_min - taper_width:
            fl[ell] = 0.0
        elif ell < ell_min:
            fl[ell] = 0.5 * (1 + np.cos(np.pi * (ell_min - ell) / taper_width))
        elif ell <= ell_max:
            fl[ell] = 1.0
        elif ell < ell_max + taper_width:
            fl[ell] = 0.5 * (1 + np.cos(np.pi * (ell - ell_max) / taper_width))
        else:
            fl[ell] = 0.0
    
    alm_filtered = hp.almxfl(alm, fl)
    return alm_filtered


def decompose_needlets(map_data, mask, lmax=2500):
    """Decompose a masked map into needlet band maps."""
    # Apply mask
    m = map_data.copy()
    m[mask < 0.5] = 0.0
    
    # Get spherical harmonic coefficients
    alm = hp.map2alm(m, lmax=lmax, use_weights=True)
    
    band_maps = []
    for ell_min, ell_max in NEEDLET_BANDS:
        alm_band = needlet_filter(alm, lmax, ell_min, ell_max)
        band_map = hp.alm2map(alm_band, NSIDE_DATA, verbose=False)
        del alm_band
        band_maps.append(band_map)

    del alm
    return band_maps


def compute_fluctuation_function(band_map, mask, q_values, n_patches=200):
    """
    Compute multifractal fluctuation function F_q for a needlet band map.
    
    Uses spherical patches (discs) at random locations instead of 1D strips.
    This is the proper spherical analogue of box-based MFDFA.
    """
    nside = hp.npix2nside(len(band_map))
    valid_pixels = np.where(mask > 0.5)[0]
    
    # Patch radii (in degrees) — multiple scales for DFA
    patch_radii_deg = [2, 4, 8, 16, 32]
    
    F_q = {q: [] for q in q_values}
    patch_sizes = []
    
    for radius_deg in patch_radii_deg:
        radius_rad = np.radians(radius_deg)
        
        # Sample random patch centers from valid pixels
        np.random.seed(42)
        center_indices = np.random.choice(valid_pixels, size=min(n_patches, len(valid_pixels)), replace=False)
        
        patch_variances = []
        for idx in center_indices:
            vec = hp.pix2vec(nside, idx)
            disc_pix = hp.query_disc(nside, vec, radius_rad)
            
            # Only use patches with sufficient valid coverage
            valid_in_disc = disc_pix[mask[disc_pix] > 0.5]
            if len(valid_in_disc) < 10:
                continue
            
            values = band_map[valid_in_disc]
            # Detrend: remove mean (0th order) — for spherical patches,
            # higher-order detrending requires spherical harmonics within patch
            # which is overkill; mean removal is standard for needlet coefficients
            var = np.var(values)
            if var > 0:
                patch_variances.append(var)
        
        if len(patch_variances) < 10:
            for q in q_values:
                F_q[q].append(np.nan)
            patch_sizes.append(radius_deg)
            continue
        
        patch_variances = np.array(patch_variances)
        patch_sizes.append(radius_deg)
        
        for q in q_values:
            if q == 0:
                fq = np.exp(0.5 * np.mean(np.log(patch_variances)))
            else:
                fq = (np.mean(patch_variances ** (q / 2))) ** (1.0 / q)
            F_q[q].append(fq)
    
    return {q: np.array(v) for q, v in F_q.items()}, np.array(patch_sizes)


def compute_hurst_exponents(F_q, patch_sizes, q_values):
    """Compute generalized Hurst exponents h(q) from F_q(s)."""
    h_q = {}
    for q in q_values:
        fq = F_q[q]
        valid = ~np.isnan(fq) & (fq > 0)
        if valid.sum() >= 3:
            slope, _, r, _, _ = stats.linregress(
                np.log(patch_sizes[valid]), np.log(fq[valid])
            )
            h_q[q] = slope
        else:
            h_q[q] = np.nan
    return h_q


_SHARED_DATA_PATH = os.path.join(OUT_DIR, '_sim_shared.npz')

# Per-worker globals (set by initializer, avoid reloading from disk each call)
_worker_cl_obs = None
_worker_tmask = None


def _init_worker():
    """Load shared data once per worker process."""
    global _worker_cl_obs, _worker_tmask
    shared = np.load(_SHARED_DATA_PATH)
    _worker_cl_obs = shared['cl_obs']
    _worker_tmask = shared['tmask']


def run_single_sim(sim_idx):
    """Worker function for parallel simulation. Must be top-level for pickling."""
    np.random.seed(sim_idx + 1000)

    sim_map = hp.synfast(_worker_cl_obs, NSIDE_DATA, new=True, verbose=False)
    sim_bands = decompose_needlets(sim_map, _worker_tmask)
    del sim_map

    band_results = {}
    for i, band in enumerate(sim_bands):
        F_q, sizes = compute_fluctuation_function(band, _worker_tmask, Q_VALUES, n_patches=100)
        h_q = compute_hurst_exponents(F_q, sizes, Q_VALUES)

        h_vals = [v for v in h_q.values() if not np.isnan(v)]
        dh = max(h_vals) - min(h_vals) if len(h_vals) >= 2 else 0
        band_results[i] = {'h_q': h_q, 'delta_h': dh}

    del sim_bands
    gc.collect()
    return sim_idx, band_results


def run_full_analysis():
    t0 = time.time()

    # ===== LOAD DATA =====
    print(f"[{time.time()-t0:.0f}s] Loading SMICA map (Nside=2048)...")
    m_K = hp.read_map(f'{OUT_DIR}/COM_CMB_IQU-smica_2048_R3.00_full.fits', field=0)
    m = m_K * 1e6  # K → μK
    tmask = hp.read_map(f'{OUT_DIR}/COM_CMB_IQU-smica_2048_R3.00_full.fits', field=3)

    fsky = np.sum(tmask > 0.5) / len(tmask)
    print(f"[{time.time()-t0:.0f}s] Map loaded: Nside={NSIDE_DATA}, fsky={fsky:.3f}")
    
    # ===== NEEDLET DECOMPOSITION OF DATA =====
    print(f"[{time.time()-t0:.0f}s] Decomposing data into {len(NEEDLET_BANDS)} needlet bands...")
    data_bands = decompose_needlets(m, tmask)
    print(f"[{time.time()-t0:.0f}s] Needlet decomposition complete.")
    
    # Band statistics
    for i, (band, (lmin, lmax)) in enumerate(zip(data_bands, NEEDLET_BANDS)):
        valid = tmask > 0.5
        print(f"  Band {i} (ℓ={lmin}-{lmax}): std={np.std(band[valid]):.2f} μK")
    
    # ===== MFDFA ON DATA =====
    print(f"\n[{time.time()-t0:.0f}s] Running MFDFA on data bands...")
    data_results = {}
    for i, (band, (lmin, lmax)) in enumerate(zip(data_bands, NEEDLET_BANDS)):
        print(f"  Band {i} (ℓ={lmin}-{lmax})...", end=" ", flush=True)
        F_q, sizes = compute_fluctuation_function(band, tmask, Q_VALUES)
        h_q = compute_hurst_exponents(F_q, sizes, Q_VALUES)
        
        h_vals = [v for v in h_q.values() if not np.isnan(v)]
        delta_h = max(h_vals) - min(h_vals) if len(h_vals) >= 2 else 0
        print(f"Δh={delta_h:.4f}")
        
        data_results[i] = {'F_q': F_q, 'sizes': sizes, 'h_q': h_q, 'delta_h': delta_h}
    
    # ===== GAUSSIAN SIMULATIONS (PARALLEL) =====
    print(f"\n[{time.time()-t0:.0f}s] Running {N_SIMS} Gaussian simulations at Nside={NSIDE_DATA} "
          f"with {N_WORKERS} parallel workers...")

    # Get observed power spectrum for simulations
    m_masked = m.copy()
    m_masked[tmask < 0.5] = 0.0
    cl_obs = hp.anafast(m_masked, lmax=2500, use_weights=True) / fsky

    # Save shared data to disk for spawn workers (avoids 50M-element pickle)
    np.savez(_SHARED_DATA_PATH, cl_obs=cl_obs, tmask=tmask)
    print(f"  Shared data saved to {_SHARED_DATA_PATH}")

    sim_delta_h = {i: [] for i in range(len(NEEDLET_BANDS))}
    sim_h_q_all = {i: {q: [] for q in Q_VALUES} for i in range(len(NEEDLET_BANDS))}

    # Simple integer args — workers load shared data from disk
    sim_args = list(range(N_SIMS))

    completed = 0
    with Pool(processes=N_WORKERS, initializer=_init_worker) as pool:
        for sim_idx, band_results in pool.imap_unordered(run_single_sim, sim_args):
            completed += 1
            if completed % 20 == 0 or completed <= 5:
                elapsed = time.time() - t0
                rate = completed / max(elapsed - 80, 1)  # subtract data processing time
                eta = (N_SIMS - completed) / rate if rate > 0 else 0
                print(f"  [{elapsed:.0f}s] Completed {completed}/{N_SIMS} "
                      f"(ETA: {eta/60:.0f} min)...", flush=True)

            for i in range(len(NEEDLET_BANDS)):
                sim_delta_h[i].append(band_results[i]['delta_h'])
                for q in Q_VALUES:
                    val = band_results[i]['h_q'].get(q, np.nan)
                    if not np.isnan(val):
                        sim_h_q_all[i][q].append(val)

            if completed % 50 == 0:
                np.savez(f'{OUT_DIR}/proper_mfdfa_checkpoint_{completed}.npz',
                         sim_delta_h={str(k): np.array(v) for k, v in sim_delta_h.items()},
                         completed=completed)
                print(f"  Checkpoint saved: {completed}/{N_SIMS}")

    print(f"\n[{time.time()-t0:.0f}s] Simulations complete.")
    
    # ===== STATISTICAL COMPARISON =====
    print(f"\n{'='*60}")
    print(f"RESULTS — Needlet-based MFDFA of Planck 2018 SMICA")
    print(f"{'='*60}")
    print(f"{'Band':>6s} {'ℓ range':>12s} {'Δh_obs':>8s} {'Δh_sim':>12s} {'σ_sim':>8s} {'Z-score':>8s} {'p-value':>10s}")
    print(f"{'-'*70}")
    
    results_summary = []
    for i, (lmin, lmax) in enumerate(NEEDLET_BANDS):
        dh_obs = data_results[i]['delta_h']
        dh_sims = np.array(sim_delta_h[i])
        dh_mean = dh_sims.mean()
        dh_std = dh_sims.std()
        
        if dh_std > 0:
            z = (dh_obs - dh_mean) / dh_std
            p = 1 - stats.norm.cdf(z)
        else:
            z = 0
            p = 1
        
        print(f"{i:>6d} {f'ℓ={lmin}-{lmax}':>12s} {dh_obs:>8.4f} {dh_mean:>8.4f}±{dh_std:.4f} {z:>8.2f}σ {p:>10.2e}")
        results_summary.append({
            'band': i, 'ell_min': lmin, 'ell_max': lmax,
            'delta_h_obs': dh_obs, 'delta_h_sim_mean': dh_mean,
            'delta_h_sim_std': dh_std, 'z_score': z, 'p_value': p
        })
    
    # ===== SAVE RESULTS =====
    np.savez(f'{OUT_DIR}/proper_mfdfa_results.npz',
             results_summary=results_summary,
             data_results={str(k): {
                 'h_q': v['h_q'], 'delta_h': v['delta_h'],
                 'sizes': v['sizes']
             } for k, v in data_results.items()},
             sim_delta_h={str(k): np.array(v) for k, v in sim_delta_h.items()},
             n_sims=N_SIMS,
             needlet_bands=NEEDLET_BANDS,
             q_values=Q_VALUES)
    print(f"\nResults saved: {OUT_DIR}/proper_mfdfa_results.npz")
    
    # ===== FIGURES =====
    print(f"\n[{time.time()-t0:.0f}s] Generating figures...")
    
    # Figure 1: Δh observed vs Gaussian null per band
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    for i, (lmin, lmax) in enumerate(NEEDLET_BANDS):
        ax = axes[i]
        dh_sims = np.array(sim_delta_h[i])
        ax.hist(dh_sims, bins=30, alpha=0.7, color='gray', edgecolor='black', density=True)
        ax.axvline(data_results[i]['delta_h'], color='red', linewidth=2, linestyle='-',
                   label=f'Observed Δh={data_results[i]["delta_h"]:.3f}')
        ax.axvline(dh_sims.mean(), color='blue', linewidth=1, linestyle='--',
                   label=f'Sim mean={dh_sims.mean():.3f}')
        z = results_summary[i]['z_score']
        ax.set_title(f'Band {i}: ℓ={lmin}-{lmax} ({z:.1f}σ)', fontsize=11)
        ax.legend(fontsize=8)
        ax.set_xlabel('Δh')
    if len(NEEDLET_BANDS) < 8:
        axes[-1].set_visible(False)
    plt.suptitle(f'Multifractal Spectrum Width: Observed vs {N_SIMS} Gaussian Simulations', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/proper_mfdfa_bands.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_mfdfa_bands.png")
    
    # Figure 2: h(q) curves — data vs simulation envelope per band
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    for i, (lmin, lmax) in enumerate(NEEDLET_BANDS):
        ax = axes[i]
        q_arr = np.array(Q_VALUES)
        h_obs = np.array([data_results[i]['h_q'].get(q, np.nan) for q in Q_VALUES])
        
        # Simulation envelope
        h_sim_low = []
        h_sim_high = []
        h_sim_mean = []
        for q in Q_VALUES:
            vals = np.array(sim_h_q_all[i][q])
            if len(vals) > 0:
                h_sim_low.append(np.percentile(vals, 2.5))
                h_sim_high.append(np.percentile(vals, 97.5))
                h_sim_mean.append(np.mean(vals))
            else:
                h_sim_low.append(np.nan)
                h_sim_high.append(np.nan)
                h_sim_mean.append(np.nan)
        
        h_sim_low = np.array(h_sim_low)
        h_sim_high = np.array(h_sim_high)
        h_sim_mean = np.array(h_sim_mean)
        
        ax.fill_between(q_arr, h_sim_low, h_sim_high, alpha=0.3, color='gray', label='95% Gaussian CI')
        ax.plot(q_arr, h_sim_mean, 'b--', linewidth=1, label='Sim mean')
        ax.plot(q_arr, h_obs, 'ro-', linewidth=2, markersize=4, label='Observed')
        ax.set_title(f'Band {i}: ℓ={lmin}-{lmax}', fontsize=11)
        ax.set_xlabel('q')
        ax.set_ylabel('h(q)')
        ax.legend(fontsize=8)
    if len(NEEDLET_BANDS) < 8:
        axes[-1].set_visible(False)
    plt.suptitle('Generalized Hurst Exponents h(q): Data vs Gaussian Envelope', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/proper_mfdfa_hq_curves.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_mfdfa_hq_curves.png")
    
    # Figure 3: Z-score summary across bands
    fig, ax = plt.subplots(figsize=(12, 6))
    band_labels = [f'ℓ={lmin}-{lmax}' for lmin, lmax in NEEDLET_BANDS]
    z_scores = [r['z_score'] for r in results_summary]
    colors = ['red' if abs(z) > 3 else 'orange' if abs(z) > 2 else 'steelblue' for z in z_scores]
    bars = ax.bar(range(len(z_scores)), z_scores, color=colors, edgecolor='black')
    ax.set_xticks(range(len(z_scores)))
    ax.set_xticklabels(band_labels, rotation=45, ha='right')
    ax.axhline(y=2, color='orange', linestyle='--', alpha=0.5, label='2σ')
    ax.axhline(y=3, color='red', linestyle='--', alpha=0.5, label='3σ')
    ax.set_ylabel('Z-score (Δh above Gaussian null)', fontsize=12)
    ax.set_title('Multifractality Significance Across Needlet Bands', fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/proper_mfdfa_zscore_summary.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_mfdfa_zscore_summary.png")
    
    # Figure 4: Singularity spectra f(α) — data vs simulation envelope
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    for i, (lmin, lmax) in enumerate(NEEDLET_BANDS):
        ax = axes[i]
        q_arr = np.array(Q_VALUES)
        h_obs = np.array([data_results[i]['h_q'].get(q, np.nan) for q in Q_VALUES])
        valid = ~np.isnan(h_obs)
        if valid.sum() < 3:
            ax.set_title(f'Band {i}: insufficient data')
            continue
        
        # τ(q) and singularity spectrum
        tau_obs = q_arr[valid] * h_obs[valid] - 1
        alpha_obs = np.gradient(tau_obs, q_arr[valid])
        f_alpha_obs = q_arr[valid] * alpha_obs - tau_obs
        
        ax.plot(alpha_obs, f_alpha_obs, 'ro-', linewidth=2, markersize=4, label='Observed')
        ax.set_title(f'Band {i}: ℓ={lmin}-{lmax}', fontsize=11)
        ax.set_xlabel('α (Hölder exponent)')
        ax.set_ylabel('f(α)')
        ax.legend(fontsize=8)
    if len(NEEDLET_BANDS) < 8:
        axes[-1].set_visible(False)
    plt.suptitle('Singularity Spectra f(α) per Needlet Band', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/proper_mfdfa_singularity.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_mfdfa_singularity.png")
    
    # Figure 5: DFA exponent (h at q=2) across bands — data vs null
    fig, ax = plt.subplots(figsize=(12, 6))
    h2_obs = [data_results[i]['h_q'].get(2, np.nan) for i in range(len(NEEDLET_BANDS))]
    h2_sim_mean = [np.mean(sim_h_q_all[i][2]) if len(sim_h_q_all[i][2]) > 0 else np.nan 
                   for i in range(len(NEEDLET_BANDS))]
    h2_sim_std = [np.std(sim_h_q_all[i][2]) if len(sim_h_q_all[i][2]) > 0 else np.nan 
                  for i in range(len(NEEDLET_BANDS))]
    
    x = np.arange(len(NEEDLET_BANDS))
    ax.errorbar(x - 0.15, h2_sim_mean, yerr=h2_sim_std, fmt='bs', markersize=6, 
                capsize=4, label='Gaussian simulations')
    ax.plot(x + 0.15, h2_obs, 'ro', markersize=8, label='Observed')
    ax.set_xticks(x)
    ax.set_xticklabels([f'ℓ={lmin}-{lmax}' for lmin, lmax in NEEDLET_BANDS], rotation=45, ha='right')
    ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5, label='White noise')
    ax.set_ylabel('h(q=2) — DFA exponent', fontsize=12)
    ax.set_title('DFA Scaling Exponent Across Needlet Bands', fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/proper_mfdfa_dfa_bands.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_mfdfa_dfa_bands.png")
    
    # Figure 6: Needlet band maps (data visualization)
    fig, axes = plt.subplots(2, 4, figsize=(24, 10))
    axes = axes.flatten()
    for i, (band, (lmin, lmax)) in enumerate(zip(data_bands, NEEDLET_BANDS)):
        band_masked = band.copy()
        band_masked[tmask < 0.5] = hp.UNSEEN
        std_val = np.std(band[tmask > 0.5])
        hp.mollview(band_masked, title=f'Band {i}: ℓ={lmin}-{lmax}', unit='μK',
                    min=-3*std_val, max=3*std_val, cmap='RdBu_r', sub=(2, 4, i+1),
                    fig=fig.number)
    if len(NEEDLET_BANDS) < 8:
        axes[-1].set_visible(False)
    plt.suptitle('SMICA Temperature — Needlet Band Decomposition', fontsize=14, y=1.02)
    plt.savefig(f'{OUT_DIR}/proper_needlet_bands_maps.png', dpi=150, bbox_inches='tight')
    plt.close('all')
    print(f"  Saved: {OUT_DIR}/proper_needlet_bands_maps.png")
    
    elapsed = time.time() - t0
    print(f"\n{'='*60}")
    print(f"ANALYSIS COMPLETE — {elapsed/60:.1f} minutes ({N_SIMS} simulations)")
    print(f"{'='*60}")
    
    # Final summary
    significant_bands = [r for r in results_summary if r['z_score'] > 2]
    highly_sig = [r for r in results_summary if r['z_score'] > 3]
    print(f"\nBands with >2σ multifractality: {len(significant_bands)}/{len(NEEDLET_BANDS)}")
    print(f"Bands with >3σ multifractality: {len(highly_sig)}/{len(NEEDLET_BANDS)}")
    
    for r in results_summary:
        if r['z_score'] > 2:
            print(f"  *** Band {r['band']} (ℓ={r['ell_min']}-{r['ell_max']}): "
                  f"Δh={r['delta_h_obs']:.4f} vs {r['delta_h_sim_mean']:.4f}±{r['delta_h_sim_std']:.4f} "
                  f"({r['z_score']:.1f}σ, p={r['p_value']:.2e})")
    
    print(f"\nAll results in: {OUT_DIR}/proper_mfdfa_results.npz")
    print("DONE")
    sys.stdout.flush()


if __name__ == '__main__':
    run_full_analysis()
