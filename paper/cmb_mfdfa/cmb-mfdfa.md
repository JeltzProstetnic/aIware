# Scale-Dependent Multifractal Structure in the Planck 2018 CMB: Evidence from Needlet-Based Detrended Fluctuation Analysis

**Matthias Gruber**

Independent Researcher, Vorarlberg, Austria
matthias@matthiasgruber.com
ORCID: 0009-0005-9697-1665
DOI: 10.5281/zenodo.20306785

## Abstract

We present the first application of multifractal detrended fluctuation analysis (MFDFA) to the Planck 2018 SMICA temperature map at full resolution (Nside = 2048). Using a needlet-based scale decomposition that respects spherical geometry, we compute generalized Hurst exponents h(q) across seven angular scale bands spanning multipoles ℓ = 2–2500. Comparing observed multifractal spectrum widths Δh against 500 Gaussian simulations with identical power spectra, we find no significant excess multifractality at large angular scales (ℓ < 100), where known CMB anomalies reside. Bands 0–2 (ℓ = 2–100) yield Z-scores of 0.33σ, −0.85σ, and −0.78σ respectively — the substantial observed multifractal spectrum widths (Δh = 0.18–0.61) are fully reproduced by Gaussian random fields with the same power spectrum, confirming that large-scale multifractality is driven by long-range correlations rather than non-Gaussian processes. At the smallest scales (ℓ = 1500–2500), we detect highly significant excess multifractality (Δh = 0.0095 vs 0.0023 ± 0.0008; Z = 9.6σ), which we tentatively attribute to non-Gaussian instrumental noise and unresolved astrophysical sources at Planck's resolution limit; confirmation requires end-to-end noise simulations. These results extend Movahed et al.'s (2011) WMAP conclusion — that CMB multifractality is correlation-driven — to the Planck era at higher resolution, confirm it across seven distinct angular scale bands via needlet decomposition, and complement Broadbridge et al.'s (2021) independent detection of multifractional behavior via Hölder exponent estimation. We discuss the implications for self-organized criticality (SOC) interpretations of cosmological initial conditions, noting that the CMB, as a recombination-era observable downstream of inflationary processing, is not expected to preserve criticality signatures from the earliest epochs.

**Keywords:** cosmic microwave background, non-Gaussianity, multifractal analysis, detrended fluctuation analysis, CMB anomalies, self-organized criticality, Planck

## 1. Introduction

The cosmic microwave background (CMB) is the oldest observable electromagnetic signal in the universe, carrying an imprint of conditions approximately 380,000 years after the Big Bang. Standard inflationary cosmology predicts that the primordial density fluctuations seeding the CMB are very nearly Gaussian, arising from quantum vacuum fluctuations stretched to macroscopic scales during inflation (Guth, 1981; Linde, 1982; Mukhanov & Chibisov, 1981). The Planck satellite's precision measurements have confirmed this prediction to extraordinary accuracy across most of the angular power spectrum (Planck Collaboration VI, 2020).

However, a persistent set of anomalies at large angular scales challenges the assumption of statistical isotropy and Gaussianity. These include: (i) a quadrupole power deficit approximately 77% below the ΛCDM expectation at 2–3σ significance (Bennett et al., 2011; Planck Collaboration VII, 2020); (ii) hemispherical power asymmetry, with the southern galactic hemisphere exhibiting approximately 10% more power than the north at 3–4σ (Eriksen et al., 2004; Planck Collaboration VII, 2020); (iii) alignment of the quadrupole and octupole moments with probability ~1–2% under isotropy (Tegmark et al., 2003; de Oliveira-Costa et al., 2004); and (iv) the CMB cold spot, a region near galactic coordinates (l, b) ≈ (210°, −57°) with minimum temperature approximately −478 μK, representing a ~3σ outlier (Vielva et al., 2004; Cruz et al., 2005).

The Planck Collaboration's comprehensive non-Gaussianity analysis (Planck Collaboration IX, 2020) applied an extensive battery of tests — including the bispectrum, trispectrum, Minkowski functionals, peak statistics, and various estimators of the local, equilateral, and orthogonal non-Gaussianity parameters — and found no significant deviations from Gaussianity for multipoles ℓ > 30. At large scales, the anomalies were confirmed but remain unexplained within standard ΛCDM.

A complementary approach to characterizing non-Gaussian structure comes from multifractal analysis, a tool from statistical physics that quantifies how scaling properties vary across different fluctuation intensities. Unlike the bispectrum, which tests for specific non-Gaussian coupling between Fourier modes, multifractal detrended fluctuation analysis (MFDFA) (Kantelhardt et al., 2002) probes the full hierarchy of scaling exponents and can detect intermittent, heterogeneous structure that standard spectral methods miss. MFDFA has proven powerful in geophysics (Kantelhardt et al., 2006), finance (Di Matteo et al., 2005), neuroscience (Ihlen, 2012), and heart rate dynamics (Ivanov et al., 1999), but has seen limited application in cosmology.

The pioneering application of MFDFA to CMB data was by Movahed, Javanmardi, Kohandel & Babar (2011), who analyzed WMAP temperature maps and detected multifractal behavior. However, they concluded that the observed multifractality was "entirely driven by long-range correlations" — i.e., fully explained by the power spectrum — rather than reflecting genuine non-Gaussian processes. Their analysis was limited by WMAP's angular resolution and sensitivity compared to Planck.

More recently, Broadbridge, Nanayakkara & Olenko (2021) applied Hölder exponent estimation to Planck CMB maps and found spatially varying scaling exponents, confirming multifractional behavior through a mathematically distinct framework. However, their approach did not employ the detrending methodology central to MFDFA and did not decompose the signal into angular scale bands.

In this work, we present the first application of MFDFA to the Planck 2018 SMICA temperature map at full resolution (Nside = 2048, approximately 50 million pixels). We introduce a methodological innovation: needlet-based scale decomposition prior to MFDFA, which (i) respects the spherical geometry of the CMB, (ii) isolates contributions from different angular scales, and (iii) enables direct comparison between the anomaly-bearing large scales and the well-behaved small scales. We compare our results against 500 Gaussian random field simulations sharing the observed power spectrum, providing rigorous statistical assessment of any detected multifractality.

The structure of this paper is as follows. Section 2 describes the Planck 2018 data products used. Section 3 details our methodology, including the needlet decomposition, the spherical MFDFA implementation, and the Gaussian simulation framework. Section 4 presents our results across seven angular scale bands. Section 5 discusses the implications, comparison with prior work, and potential systematic effects. Section 6 summarizes our conclusions.

## 2. Data

### 2.1 Planck 2018 SMICA Temperature Map

We use the Planck 2018 SMICA (Spectral Matching Independent Component Analysis) full-mission temperature map at HEALPix resolution Nside = 2048, corresponding to 50,331,648 pixels and an angular resolution of approximately 5 arcminutes (Planck Collaboration IV, 2020). The SMICA pipeline combines all nine Planck frequency channels (30–857 GHz) to produce a minimum-variance CMB temperature estimate with optimal foreground subtraction (Delabrouille et al., 2009).

The map is distributed in Kelvin (K_CMB) and was converted to microkelvin (μK) for all analyses. The full-sky RMS temperature fluctuation is 108.4 μK, consistent with the expected CMB signal amplitude.

We apply the accompanying SMICA temperature confidence mask (TMASK), which excludes 15.8% of the sky — primarily the galactic plane and point source regions — leaving an effective sky fraction f_sky = 0.842. All analyses are performed consistently on masked data, and Gaussian simulations are subjected to identical masking.

The data file used is `COM_CMB_IQU-smica_2048_R3.00_full.fits`, obtained from the Planck Legacy Archive (PLA) via the NASA/IPAC Infrared Science Archive.

### 2.2 Published Power Spectrum

For pipeline validation, we use the Planck 2018 TT power spectrum (`COM_PowerSpect_CMB-TT-full_R3.01.txt`), containing 2,507 multipole measurements from ℓ = 2 to ℓ = 2508 with asymmetric error bars. We independently verify consistency between the map-derived spectrum (via `anafast`) and the published spectrum.

## 3. Methods

### 3.1 Pipeline Validation

Before performing the multifractal analysis, we validate our computational pipeline by comparing the observed Planck TT power spectrum against the theoretical ΛCDM prediction. We generate the theory spectrum using CAMB (Code for Anisotropies in the Microwave Background; Lewis, Challinor & Lasenby, 2000) with Planck 2018 best-fit cosmological parameters: H_0 = 67.36 km/s/Mpc, Ω_b h² = 0.02237, Ω_c h² = 0.1200, τ = 0.0544, A_s = 2.1 × 10⁻⁹, n_s = 0.9649 (Planck Collaboration VI, 2020).

We compute the goodness-of-fit statistic χ²/dof and examine residuals, with particular attention to the low-ℓ regime (ℓ ≤ 30) where the known anomalies reside.

### 3.2 Needlet Decomposition

To analyze multifractal structure as a function of angular scale, we decompose the SMICA temperature map into seven needlet bands using band-pass filtering in spherical harmonic space. Needlets are a class of spherical wavelets that provide a natural, localized basis on the sphere with exact reconstruction properties (Narcowich, Petrushev & Ward, 2006; Marinucci et al., 2008).

For a masked temperature map T(n̂), we first compute the spherical harmonic coefficients aℓm up to ℓmax = 2500 using the HEALPix `map2alm` routine with quadrature weights. For each band j defined by multipole range [ℓmin⁽ʲ⁾, ℓmax⁽ʲ⁾], we apply a smooth cosine-tapered band-pass filter fℓ⁽ʲ⁾ defined piecewise:

- fℓ⁽ʲ⁾ = 0 for ℓ < ℓmin⁽ʲ⁾ − Δ (below band)
- fℓ⁽ʲ⁾ = ½(1 + cos(π(ℓmin⁽ʲ⁾ − ℓ)/Δ)) for ℓmin⁽ʲ⁾ − Δ ≤ ℓ < ℓmin⁽ʲ⁾ (lower taper)
- fℓ⁽ʲ⁾ = 1 for ℓmin⁽ʲ⁾ ≤ ℓ ≤ ℓmax⁽ʲ⁾ (passband)
- fℓ⁽ʲ⁾ = ½(1 + cos(π(ℓ − ℓmax⁽ʲ⁾)/Δ)) for ℓmax⁽ʲ⁾ < ℓ ≤ ℓmax⁽ʲ⁾ + Δ (upper taper)
- fℓ⁽ʲ⁾ = 0 for ℓ > ℓmax⁽ʲ⁾ + Δ (above band)

where Δ = max(5, (ℓmax⁽ʲ⁾ − ℓmin⁽ʲ⁾)/10) is the taper width, chosen to avoid Gibbs ringing while maintaining sharp band separation. The filtered coefficients ãℓm⁽ʲ⁾ = fℓ⁽ʲ⁾ · aℓm are then transformed back to pixel space via `alm2map`.

Our seven bands are defined as:

| Band | ℓ range | Angular scale | Physical regime |
|------|---------|---------------|-----------------|
| 0 | 2–10 | >18° | Anomaly regime (quadrupole, octupole) |
| 1 | 10–30 | 6°–18° | Large-scale anomalies |
| 2 | 30–100 | 1.8°–6° | Intermediate scales |
| 3 | 100–300 | 0.6°–1.8° | First acoustic peak |
| 4 | 300–800 | 0.23°–0.6° | Acoustic oscillations |
| 5 | 800–1500 | 0.12°–0.23° | Damping tail |
| 6 | 1500–2500 | 0.07°–0.12° | Small scales |

This logarithmic spacing ensures approximately uniform coverage in log(ℓ), with finer subdivision at the large scales where anomalies are concentrated.

### 3.3 Spherical MFDFA

Standard MFDFA (Kantelhardt et al., 2002) is defined for one-dimensional time series, where the signal is divided into non-overlapping segments, locally detrended, and the q-th order fluctuation function Fq(s) is computed as a function of segment size s. The generalized Hurst exponent h(q) is then extracted from the scaling relation Fq(s) ∝ s^h(q).

We adapt MFDFA to the sphere by replacing linear segments with spherical disc patches. For each needlet band map B_j(n̂):

1. **Patch sampling.** We randomly sample N_p = 200 patch center locations from valid (unmasked) pixels. For each center, we extract circular disc patches at radii r ∈ {2°, 4°, 8°, 16°, 32°}, providing five scale levels.

2. **Detrending.** Within each patch, we remove the mean temperature (zeroth-order detrending). For needlet coefficient maps, which are already band-limited, mean removal is sufficient — higher-order polynomial detrending on the sphere would require spherical harmonic fitting within each patch, introducing unnecessary complexity without significant benefit for band-passed signals.

3. **Fluctuation function.** For each scale r and moment order q, we compute:

> Fq(r) = ( (1/Np) Σk σk^q )^(1/q)    for q ≠ 0
>
> F₀(r) = exp( (1/2Np) Σk ln σk² )      for q = 0

where σk² is the variance of the detrended temperature values within the k-th patch at scale r, and the sum runs over all Np valid patches. Patches with fewer than 10 valid pixels (due to masking) are excluded.

4. **Hurst exponents.** The generalized Hurst exponent h(q) is extracted from the scaling relation ln Fq(r) = h(q) ln r + cq via ordinary least squares regression across the five scale levels. We compute h(q) for q ∈ {−5, −4, ..., 4, 5}.

5. **Multifractal spectrum width.** The key summary statistic is the multifractal spectrum width Δh = maxq h(q) − minq h(q). A monofractal (Gaussian random) field has Δh ≈ 0 (constant h(q) ≈ 0.5 for white noise). Multifractal fields have Δh > 0, with larger values indicating stronger multifractality. SOC systems typically exhibit Δh > 0.2 (Kantelhardt et al., 2002).

6. **Singularity spectrum.** From h(q), we derive the Legendre-transformed singularity spectrum f(α) via: τ(q) = q·h(q) − 1, then α = dτ/dq, and f(α) = q·α − τ(q). The width of f(α) characterizes the range of Hölder exponents present in the field, providing a complementary characterization of multifractal structure.

### 3.4 Gaussian Null Simulations

To assess the statistical significance of observed multifractality, we generate N_sim = 500 Gaussian random field realizations at the same resolution (Nside = 2048) using HEALPix `synfast`. Each realization shares the observed angular power spectrum C_ℓ (corrected for the sky fraction f_sky = 0.842), ensuring that any detected multifractality cannot be attributed to the power spectrum alone — i.e., to long-range correlations in the Gaussian sense.

Each simulation is subjected to identical processing: the same TMASK is applied, the same needlet decomposition is performed, and the same MFDFA pipeline is run. This yields a null distribution of Δh for each band, against which the observed Δh is compared.

We report Z-scores (number of standard deviations above the Gaussian mean) and one-sided p-values for each band, with the null hypothesis being that the CMB is a Gaussian random field with the observed power spectrum.

The 500 simulations were executed in parallel across 8 CPU cores with total computation time of approximately 1.9 hours on a consumer workstation (AMD Ryzen, 48 GB RAM, WSL2/Ubuntu).

## 4. Results

### 4.1 Pipeline Validation

The ΛCDM best-fit spectrum provides an excellent fit to the observed Planck 2018 TT power spectrum, with χ²/dof = 1.031 (2507 data points, 6 parameters). The first acoustic peak is located at ℓ = 220 with amplitude D_ℓ = 5732 μK², consistent with Planck Collaboration VI (2020).

At low multipoles, we confirm the known anomalies:

| Multipole | D_ℓ (observed) | D_ℓ (ΛCDM) | Deficit | Significance |
|-----------|---------------|------------|---------|-------------|
| ℓ = 2 | 225.9 μK² | 1022.5 μK² | 77.9% | −2.39σ |
| ℓ = 3 | 936.9 μK² | 968.4 μK² | 3.2% | −0.04σ |
| ℓ = 4 | 692.2 μK² | 916.4 μK² | 24.5% | −0.47σ |
| ℓ = 5 | 1501.7 μK² | 877.6 μK² | (excess) | +0.72σ |
| ℓ = 20 | 659.9 μK² | 906.6 μK² | 27.2% | −1.44σ |

The mean normalized residual for ℓ ≤ 30 is −0.51, confirming the systematic low-ℓ power suppression.

### 4.2 SMICA Map Properties

The SMICA temperature map at Nside = 2048 has a full-sky RMS of 108.4 μK. After applying the temperature confidence mask (f_sky = 0.842):

**Hemispherical asymmetry.** The northern galactic hemisphere RMS is 105.2 μK while the southern is 110.1 μK, yielding a power ratio S²/N² = 1.095 and asymmetry parameter A = (N − S)/(N + S) = −0.023. This is consistent with the documented hemispherical power asymmetry (Planck Collaboration VII, 2020).

**Cold spot.** The region centered at galactic coordinates (l, b) ≈ (210°, −57°) shows a mean temperature of −108.3 μK (−1.01σ) within 5° radius, with a minimum pixel temperature of −477.6 μK (−4.44σ).

### 4.3 Needlet Band Decomposition

The needlet decomposition yields band maps with the following RMS amplitudes:

| Band | ℓ range | RMS (μK) |
|------|---------|----------|
| 0 | 2–10 | 32.4 |
| 1 | 10–30 | 32.6 |
| 2 | 30–100 | 45.7 |
| 3 | 100–300 | 71.9 |
| 4 | 300–800 | 48.6 |
| 5 | 800–1500 | 24.7 |
| 6 | 1500–2500 | 9.8 |

Band 3 (ℓ = 100–300) dominates, as expected from the first acoustic peak. The low-ℓ bands (0–1) carry substantial power despite spanning few multipoles, reflecting the well-known low-ℓ plateau of the CMB power spectrum.

### 4.4 Multifractal Analysis

#### 4.4.1 Observed Multifractal Spectrum Widths

The multifractal spectrum width Δh = max_q h(q) − min_q h(q) measures the degree of multifractality in each needlet band. The observed values from the SMICA map are:

| Band | ℓ range | Δh (observed) |
|------|---------|---------------|
| 0 | 2–10 | 0.6101 |
| 1 | 10–30 | 0.4368 |
| 2 | 30–100 | 0.1819 |
| 3 | 100–300 | 0.0399 |
| 4 | 300–800 | 0.0065 |
| 5 | 800–1500 | 0.0035 |
| 6 | 1500–2500 | 0.0095 |

Multifractal spectrum width decreases monotonically from Band 0 to Band 5, reflecting the decreasing range of spatial correlations within progressively narrower harmonic bands. Band 6 breaks this trend with a spectrum width approximately 2.7× larger than Band 5, despite spanning the smallest angular scales.

#### 4.4.2 Gaussian Null Distribution

The 500 Gaussian simulations with matched power spectra yield the following null distributions for Δh:

| Band | ℓ range | Δh_sim (mean ± σ) | 95% CI |
|------|---------|-------------------|--------|
| 0 | 2–10 | 0.5618 ± 0.1444 | [0.28, 0.85] |
| 1 | 10–30 | 0.5359 ± 0.1163 | [0.31, 0.76] |
| 2 | 30–100 | 0.2265 ± 0.0572 | [0.12, 0.34] |
| 3 | 100–300 | 0.0339 ± 0.0054 | [0.023, 0.045] |
| 4 | 300–800 | 0.0071 ± 0.0010 | [0.005, 0.009] |
| 5 | 800–1500 | 0.0029 ± 0.0004 | [0.002, 0.004] |
| 6 | 1500–2500 | 0.00233 ± 0.00075 | [0.001, 0.004] |

The Gaussian null itself exhibits substantial multifractal spectrum widths at large scales (Bands 0–2), with Δh_sim = 0.23–0.56. This is a critical finding: Gaussian random fields with the observed CMB power spectrum naturally produce apparent multifractality through long-range correlations alone. Any claim of non-Gaussian multifractality in the CMB must demonstrate excess above these baseline values, not merely non-zero Δh.

#### 4.4.3 Statistical Significance

Comparing observed Δh against the Gaussian null:

| Band | ℓ range | Δh_obs | Δh_sim (mean ± σ) | Z-score | p-value |
|------|---------|--------|-------------------|---------|---------|
| 0 | 2–10 | 0.6101 | 0.5618 ± 0.1444 | +0.33σ | 0.37 |
| 1 | 10–30 | 0.4368 | 0.5359 ± 0.1163 | −0.85σ | 0.80 |
| 2 | 30–100 | 0.1819 | 0.2265 ± 0.0572 | −0.78σ | 0.78 |
| 3 | 100–300 | 0.0399 | 0.0339 ± 0.0054 | +1.09σ | 0.14 |
| 4 | 300–800 | 0.0065 | 0.0071 ± 0.0010 | −0.60σ | 0.73 |
| 5 | 800–1500 | 0.0035 | 0.0029 ± 0.0004 | +1.36σ | 0.086 |
| 6 | 1500–2500 | 0.00951 | 0.00233 ± 0.00075 | +9.56σ | <10⁻²⁰ |

Bands 0–5 are fully consistent with the Gaussian null hypothesis, with Z-scores ranging from −0.85σ to +1.36σ. No band in the range ℓ = 2–1500 shows significant excess multifractality.

Band 6 (ℓ = 1500–2500) is a dramatic outlier at 9.56σ, with observed Δh approximately 4× the Gaussian expectation. This detection is discussed in §5.6.

#### 4.4.4 Generalized Hurst Exponents

Figure 2 presents the generalized Hurst exponent curves h(q) for q ∈ {−5, ..., 5} in each band, with the 95% confidence interval from Gaussian simulations shown as the shaded envelope.

For Bands 0–2 (ℓ < 100), the observed h(q) curves lie within the Gaussian envelope across all q values. The curves exhibit the expected monotonically decreasing shape: h(q) ranges from ~1.3 at q = −5 to ~0.7 at q = +5 for Band 0, reflecting the varying sensitivity of different q-moments to fluctuation intensity. Crucially, the Gaussian simulations reproduce this variation entirely — the shape is a consequence of long-range correlations in the power spectrum, not of non-Gaussian processes.

For Bands 3–5 (ℓ = 100–1500), h(q) curves are nearly flat (Δh < 0.04), consistent with the narrow bandwidths suppressing cross-scale correlations. Data and simulations agree closely.

For Band 6 (ℓ = 1500–2500), the observed h(q) curve is substantially steeper than the Gaussian envelope. The deviation is symmetric: h(q) exceeds the Gaussian CI for q < 0 (small fluctuations) and falls below it for q > 0 (large fluctuations). This symmetric steepening of the h(q) curve is characteristic of heterogeneous noise contamination rather than a primordial non-Gaussian signal, which would typically shift the entire curve rather than change its slope.

#### 4.4.5 Singularity Spectra

The Legendre-transformed singularity spectra f(α) confirm the h(q) analysis. Bands 0–2 show broad f(α) curves (wide range of Hölder exponents), but indistinguishable from the Gaussian null. Band 6 exhibits a wider f(α) than any Gaussian simulation, with Hölder exponents spanning a range approximately 4× the Gaussian expectation.

### 4.5 DFA Scaling Exponents

The DFA scaling exponent h(q = 2) characterizes the dominant correlation structure within each needlet band. Figure 5 compares observed and simulated h(2) values:

| Band | ℓ range | h(2) observed | h(2) simulations |
|------|---------|---------------|------------------|
| 0 | 2–10 | 0.757 | 0.753 ± 0.026 |
| 1 | 10–30 | 0.410 | 0.398 ± 0.020 |
| 2 | 30–100 | 0.054 | 0.063 ± 0.011 |
| 3–6 | 100–2500 | ≈0.00 | ≈0.00 |

Band 0 (ℓ = 2–10) exhibits h(2) = 0.757, indicating strong long-range power-law correlations well above white noise (h = 0.5). This is consistent with the red power spectrum at the largest scales. Band 1 (ℓ = 10–30) shows h(2) = 0.410, below the white noise threshold — a consequence of band-pass filtering, which suppresses the cross-scale correlations that generate apparent persistence. Bands 3–6 have h(2) ≈ 0, expected for narrow band-passed signals where the within-band structure approaches uncorrelated.

In all bands, the observed h(2) is indistinguishable from the Gaussian simulations, confirming that the correlation structure of the CMB is fully consistent with a Gaussian random field at all angular scales probed.

## 5. Discussion

### 5.1 Comparison with Movahed et al. (2011)

Movahed et al. applied MFDFA to WMAP temperature maps and detected multifractal behavior, but concluded it was "entirely driven by long-range correlations" — i.e., the power spectrum alone could explain the observed multifractality. Their Gaussian shuffled surrogates destroyed the correlations and eliminated the multifractality, while phase-randomized surrogates (preserving correlations but destroying non-Gaussianity) reproduced it.

Our analysis differs in three critical respects:

1. **Higher resolution.** Planck's Nside = 2048 provides approximately 4× finer angular resolution than WMAP, potentially revealing non-Gaussian structure below WMAP's resolution limit.

2. **Scale decomposition.** By decomposing into needlet bands, we isolate the contribution of each angular scale to the total multifractality. This reveals whether the signal is concentrated at specific scales or distributed uniformly.

3. **Matched-spectrum null.** Our Gaussian simulations share the exact observed C_ℓ, ensuring that any excess multifractality cannot be attributed to the power spectrum. If our results show significant Δh above the Gaussian null, this directly contradicts Movahed et al.'s conclusion — at least for Planck-resolution data.

Our results strongly confirm Movahed et al.'s conclusion and extend it in two important respects. First, the conclusion holds at Planck resolution (Nside = 2048, approximately 4× finer than WMAP), ruling out the possibility that WMAP's angular resolution masked non-Gaussian multifractal structure at intermediate scales. Second, our needlet-based scale decomposition demonstrates that the conclusion holds independently within each angular scale band from ℓ = 2 to ℓ = 1500 — the correlation-driven nature of CMB multifractality is not a scale-averaged artifact but a robust property at every scale probed.

The Gaussian simulations in Bands 0–2 produce multifractal spectrum widths of Δh = 0.23–0.56, comparable to or exceeding the observed values. This underscores a methodological point: reporting non-zero Δh in the CMB without comparison to matched-spectrum Gaussian simulations is insufficient to establish non-Gaussian multifractality. The power spectrum alone, through its long-range correlation structure, generates substantial apparent multifractality.

### 5.2 Comparison with Broadbridge et al. (2021)

Broadbridge, Nanayakkara & Olenko estimated pointwise Hölder exponents on Planck maps and found spatial variation, confirming multifractional behavior. Our MFDFA approach is methodologically complementary: while Hölder exponents characterize local regularity, MFDFA characterizes the global scaling hierarchy. Finding consistent multifractal structure through both approaches would constitute robust, method-independent evidence.

### 5.3 Relationship to Planck Non-Gaussianity Analysis

The Planck Collaboration's non-Gaussianity tests (Planck Collaboration IX, 2020) focused primarily on primordial non-Gaussianity parameters (f_NL in local, equilateral, and orthogonal configurations), Minkowski functionals, and n-point correlation functions. MFDFA tests for a different aspect of non-Gaussian structure: the heterogeneity of scaling behavior across fluctuation intensities. Our results indicate that, for angular scales ℓ = 2–1500, MFDFA agrees with the Planck team's conclusion: the CMB temperature field is consistent with a Gaussian random field.

The sole exception — excess multifractality at ℓ > 1500 — is at scales where the Planck Collaboration themselves note increased systematic effects from beam asymmetry, unresolved point sources, and correlated noise (Planck Collaboration IV, 2020). Our detection is consistent with these known contamination sources rather than with primordial non-Gaussianity.

This result also carries a methodological lesson for the broader MFDFA community: in fields where MFDFA has revealed intermittent dynamics invisible to spectral methods — turbulence (Muzy, Bacry & Arnéodo, 1991), cardiac dynamics (Ivanov et al., 1999), neural signals (Ihlen, 2012) — the underlying processes are intrinsically nonlinear. The CMB, by contrast, is to excellent approximation a linearly processed Gaussian random field. MFDFA's power to detect non-Gaussianity does not imply that every signal harbors non-Gaussian structure; the tool must be calibrated against matched-spectrum Gaussian surrogates before drawing conclusions.

### 5.4 Scale Dependence and the CMB Anomalies

The absence of excess multifractality at large angular scales (ℓ < 100) constrains the nature of the known CMB anomalies. The quadrupole deficit, hemispherical asymmetry, quadrupole-octupole alignment, and cold spot — all residing at ℓ < 30 — do not manifest as multifractal excess above the Gaussian null. Specifically, Band 0 (ℓ = 2–10, which contains the anomalous quadrupole and octupole) yields Z = +0.33σ, while Band 1 (ℓ = 10–30, spanning the remainder of the anomalous regime) yields Z = −0.85σ.

This result does not diminish the significance of the anomalies themselves — they remain 2–4σ outliers in the power spectrum and alignment statistics. Rather, it indicates that the anomalies are not accompanied by multifractal structure beyond what the power spectrum predicts. In other words, the anomalous *amplitudes* at low ℓ (the power deficit) and the anomalous *geometry* (the alignments) do not imply anomalous *scaling heterogeneity*. These are distinct statistical properties, and the anomalies appear to be confined to the first two — the amplitude and geometric domains — without extending to the multifractal domain.

This constrains physical models that predict the anomalies arise from a fundamentally non-Gaussian process such as a topological defect, anisotropic inflation, or a nonlinear pre-inflationary mechanism. If such a process were responsible, one would generically expect it to produce not only anomalous amplitudes but also anomalous scaling structure. The absence of the latter favors explanations in which the anomalies are either (i) statistical fluctuations within a Gaussian framework, (ii) produced by a mechanism that affects only the lowest moments without introducing multifractal structure, or (iii) too weak to be detected by MFDFA at current sensitivity.

### 5.5 Connection to Self-Organized Criticality

Models in which the universe exhibits self-organized criticality (SOC) (Bak, Tang & Wiesenfeld, 1987; Jensen, 1998) predict scale-free correlations, power-law dynamics, and multifractal measures — signatures that MFDFA is specifically designed to detect. Our null result at large scales (Bands 0–5) does not detect these signatures in the CMB beyond what the Gaussian power spectrum explains.

However, this null result does not bear directly on the SOC hypothesis for cosmological initial conditions, for a fundamental reason: the CMB is not a direct observable of the initial conditions. The CMB temperature anisotropies are the photon-baryon decoupling signature at redshift z ≈ 1100, approximately 380,000 years after the Big Bang. Between the initial conditions and the CMB, the primordial perturbations are processed through: (i) inflationary dynamics, which exponentially stretch pre-existing structure and generate nearly Gaussian perturbations from quantum vacuum fluctuations; (ii) reheating; (iii) radiation-dominated and matter-dominated evolution; and (iv) photon-baryon acoustic oscillations and diffusion damping up to recombination.

This chain of predominantly linear physical processes acts as a Gaussian filter on the initial conditions. Even if the initial state of the universe exhibited SOC with characteristic multifractal structure — as proposed in computational cosmology frameworks (Gruber, 2026) — inflation alone would suppress non-Gaussian signatures by factors of order e⁻²ᴺ where N ≈ 60 is the number of e-folds, rendering them undetectable in the CMB.

The appropriate observational targets for primordial criticality signatures are therefore not the CMB temperature field but rather: (i) primordial gravitational waves (B-mode polarization), which bypass the photon-baryon fluid entirely and may preserve pre-inflationary structure; (ii) primordial non-Gaussianity in the CMB at higher order (trispectrum and beyond), where inflationary suppression is weaker; and (iii) the large-scale structure of the universe at late times, where nonlinear gravitational evolution may regenerate complexity from initially subtle deviations.

Our DFA scaling exponents at large scales — h(2) = 0.757 for Band 0 (ℓ = 2–10) — fall in the regime of strong long-range correlations characteristic of SOC systems. However, the Gaussian simulations reproduce these exponents exactly (h(2)_sim = 0.753 ± 0.026), demonstrating that the observed correlation structure is fully consistent with the standard inflationary power spectrum without invoking SOC dynamics.

### 5.6 The Small-Scale Detection (ℓ = 1500–2500)

The 9.6σ excess multifractality in Band 6 demands careful interpretation. Several lines of evidence indicate this detection is of instrumental or astrophysical origin rather than primordial:

**Noise non-Gaussianity.** Our Gaussian simulations model the CMB signal faithfully but assume perfectly Gaussian noise. In reality, Planck's noise at ℓ > 1500 is substantially non-Gaussian due to the scanning strategy (correlated 1/f noise along scan rings), destriping residuals, and the non-uniform hit count across the sky. The SMICA pipeline mitigates but does not eliminate these effects (Planck Collaboration IV, 2020). Any residual non-Gaussian noise structure would produce excess Δh in the data relative to our idealized Gaussian null, precisely as observed.

**Unresolved point sources.** At ℓ > 1500, the contribution of unresolved radio and infrared point sources becomes non-negligible. Point sources are intrinsically non-Gaussian (Poisson-distributed), and while the brightest are masked and statistical source corrections are applied, residual point source contamination at the faint end contributes non-Gaussian structure at the smallest scales.

**h(q) curve morphology.** The observed h(q) in Band 6 shows symmetric steepening relative to the Gaussian envelope — the deviation is approximately equal for negative q (small fluctuations) and positive q (large fluctuations). This symmetric pattern is characteristic of heterogeneous noise contamination, which affects the full dynamic range of the signal. A primordial non-Gaussian signal would more typically shift the h(q) curve or produce asymmetric deviations (e.g., excess only for positive q if driven by rare hot spots).

**Definitive test.** To distinguish instrumental from primordial non-Gaussianity at these scales, the analysis should be repeated using the Planck FFP10 end-to-end simulations, which model the full instrument response including correlated noise, beam effects, and the component separation pipeline. If the FFP10 null distribution encompasses the observed Δh, the detection is instrumental. This test is beyond the scope of the present work but represents the natural follow-up.

### 5.7 Potential Systematic Effects

We consider several potential sources of spurious multifractality:

**Gravitational lensing.** Weak gravitational lensing by large-scale structure introduces mild non-Gaussianity into the CMB. However, lensing primarily affects small scales (ℓ > 500) through mode coupling, whereas our detected multifractality is concentrated at ℓ < 100. Lensing is therefore unlikely to explain our signal.

**Foreground residuals.** The SMICA pipeline is not perfect, and foreground residuals (particularly from thermal dust and synchrotron emission) may persist in the cleaned map. We mitigate this by applying the confidence mask, which excludes the most contaminated regions. However, low-level foreground contamination at high galactic latitudes could contribute to non-Gaussian structure. A definitive test would require repeating the analysis on the SEVEM, NILC, and Commander component-separated maps to check for pipeline dependence.

**Masking artifacts.** The galactic mask itself introduces mode coupling that could mimic non-Gaussian structure. Our use of Gaussian simulations with identical masking should account for this effect, but edge effects near the mask boundary may warrant further investigation.

**Integrated Sachs-Wolfe (ISW) effect.** The late-time ISW effect introduces correlated large-scale fluctuations from the decay of gravitational potentials in a dark-energy-dominated universe. This is a real physical effect (not a systematic) and could contribute to non-Gaussian structure at ℓ < 30. Separating the ISW contribution would require cross-correlation with galaxy surveys, which is beyond the scope of this work.

### 5.8 Limitations

Our spherical MFDFA implementation uses disc patches rather than the box-based segmentation of standard 1D MFDFA. While this is a natural adaptation to the sphere, it introduces several differences: patches overlap at large radii, the number of pixels per patch varies with position (due to HEALPix pixelization), and the detrending is limited to mean removal. A more rigorous implementation would employ spherical harmonic detrending within each patch, at the cost of substantially increased computational complexity.

The five patch radii (2°–32°) provide limited scale sampling compared to the hundreds of segment sizes available in 1D MFDFA. This constrains the accuracy of h(q) extraction. Future work could employ a finer radius grid or adopt wavelet-based multifractal formalism directly on the sphere.

## 6. Conclusions

We have presented the first application of needlet-based multifractal detrended fluctuation analysis (MFDFA) to the Planck 2018 SMICA temperature map at full resolution (Nside = 2048), with comparison against 500 Gaussian random field simulations sharing the observed power spectrum. Our main findings are:

1. **No excess multifractality at large scales.** Bands 0–5 (ℓ = 2–1500) show multifractal spectrum widths fully consistent with the Gaussian null hypothesis. The substantial apparent multifractality at large scales (Δh = 0.18–0.61 for ℓ < 100) is entirely attributable to long-range correlations encoded in the power spectrum. This extends and confirms Movahed et al.'s (2011) WMAP result at 4× higher angular resolution and across seven independent scale bands.

2. **Excess multifractality at the smallest scales.** Band 6 (ℓ = 1500–2500) shows 9.6σ excess with Δh approximately 4× the Gaussian expectation. The morphology of the h(q) deviation and the scale regime implicate non-Gaussian instrumental noise and unresolved astrophysical sources rather than primordial physics. Confirmation requires Planck FFP10 end-to-end simulations.

3. **DFA exponents consistent with Gaussian field.** The scaling exponents h(q = 2) match between data and simulations in all bands, from h(2) = 0.757 at ℓ = 2–10 (strong long-range correlations) to h(2) ≈ 0 at ℓ > 100 (band-pass suppression). No band shows anomalous scaling behavior.

4. **CMB anomalies are not multifractal.** The known large-scale anomalies (quadrupole deficit, hemispherical asymmetry, quadrupole-octupole alignment, cold spot) do not manifest as excess multifractal structure. Their anomalous character is confined to the amplitude and geometric domains, not the scaling domain.

5. **CMB constrains but does not test primordial criticality.** For models invoking self-organized criticality in cosmological initial conditions, the CMB is too far downstream of the initial state — separated by inflationary processing, reheating, and 380,000 years of linear plasma physics — to preserve multifractal signatures. Observational tests of primordial criticality should target B-mode polarization, higher-order non-Gaussianity parameters, or late-time nonlinear structure.

This work demonstrates both the power and the limitations of MFDFA as applied to the CMB. The technique successfully characterizes the full multifractal structure of the Planck temperature field across all angular scales and identifies a significant small-scale detection. However, the dominant contribution to apparent CMB multifractality is the power spectrum itself — a result that underscores the importance of matched-spectrum Gaussian null simulations in any multifractal analysis of cosmological data.

**Data availability.** All Planck 2018 data products are publicly available from the Planck Legacy Archive (https://pla.esac.esa.int/). Analysis code will be made available upon publication.

**Acknowledgments.** This work uses observations obtained by Planck (http://www.esa.int/Planck), an ESA science mission with instruments and contributions directly funded by ESA Member States, NASA, and Canada. Computations were performed using HEALPix (Górski et al., 2005), CAMB (Lewis et al., 2000), NumPy (Harris et al., 2020), SciPy (Virtanen et al., 2020), and Matplotlib (Hunter, 2007).

## References

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59(4), 381–384.

Bennett, C. L., et al. (2011). Seven-year Wilkinson Microwave Anisotropy Probe (WMAP) observations: Are there cosmic microwave background anomalies? *The Astrophysical Journal Supplement Series*, 192(2), 17.

Broadbridge, P., Nanayakkara, T., & Olenko, A. (2021). On multifractionality of spherical random fields with cosmological applications. arXiv:2104.13945.

Cruz, M., Martínez-González, E., Vielva, P., & Cayón, L. (2005). Detection of a non-Gaussian spot in WMAP. *Monthly Notices of the Royal Astronomical Society*, 356(1), 29–40.

de Oliveira-Costa, A., Tegmark, M., Zaldarriaga, M., & Hamilton, A. (2004). Significance of the largest scale CMB fluctuations in WMAP. *Physical Review D*, 69(6), 063516.

Delabrouille, J., Cardoso, J.-F., Le Jeune, M., Betoule, M., Fay, G., & Guilloux, F. (2009). A full sky, low foreground, high resolution CMB map from WMAP. *Astronomy & Astrophysics*, 493(3), 835–857.

Di Matteo, T., Aste, T., & Dacorogna, M. M. (2005). Long-term memories of developed and emerging markets: Using the scaling analysis to characterize their stage of development. *Journal of Banking & Finance*, 29(4), 827–851.

Eriksen, H. K., Hansen, F. K., Banday, A. J., Górski, K. M., & Lilje, P. B. (2004). Asymmetries in the cosmic microwave background anisotropy field. *The Astrophysical Journal*, 605(1), 14–20.

Górski, K. M., Hivon, E., Banday, A. J., Wandelt, B. D., Hansen, F. K., Reinecke, M., & Bartelmann, M. (2005). HEALPix: A framework for high-resolution discretization and fast analysis of data distributed on the sphere. *The Astrophysical Journal*, 622(2), 759–771.

Gruber, M. (2026). Self-Bootstrapping Hypersurface of a Class 4 Automaton (SB-HC4A): A computational cosmology framework. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18698605

Guth, A. H. (1981). Inflationary universe: A possible solution to the horizon and flatness problems. *Physical Review D*, 23(2), 347–356.

Harris, C. R., et al. (2020). Array programming with NumPy. *Nature*, 585(7825), 357–362.

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90–95.

Ihlen, E. A. F. (2012). Introduction to multifractal detrended fluctuation analysis in Matlab. *Frontiers in Physiology*, 3, 141.

Ivanov, P. C., Amaral, L. A. N., Goldberger, A. L., Havlin, S., Rosenblum, M. G., Struzik, Z. R., & Stanley, H. E. (1999). Multifractality in human heartbeat dynamics. *Nature*, 399(6735), 461–465.

Jensen, H. J. (1998). *Self-Organized Criticality: Emergent Complex Behavior in Physical and Biological Systems*. Cambridge University Press.

Kantelhardt, J. W., Zschiegner, S. A., Koscielny-Bunde, E., Havlin, S., Bunde, A., & Stanley, H. E. (2002). Multifractal detrended fluctuation analysis of nonstationary time series. *Physica A*, 316(1–4), 87–114.

Kantelhardt, J. W., Koscielny-Bunde, E., Rybski, D., Braun, P., Bunde, A., & Havlin, S. (2006). Long-term persistence and multifractality of precipitation and river runoff records. *Journal of Geophysical Research: Atmospheres*, 111(D1).

Lewis, A., Challinor, A., & Lasenby, A. (2000). Efficient computation of cosmic microwave background anisotropies in closed Friedmann-Robertson-Walker models. *The Astrophysical Journal*, 538(2), 473–476.

Linde, A. D. (1982). A new inflationary universe scenario: A possible solution of the horizon, flatness, homogeneity, isotropy and primordial monopole problems. *Physics Letters B*, 108(6), 389–393.

Marinucci, D., Pietrobon, D., Balbi, A., Baldi, P., Cabella, P., Kerkyacharian, G., ... & Picard, D. (2008). Spherical needlets for cosmic microwave background data analysis. *Monthly Notices of the Royal Astronomical Society*, 383(2), 539–545.

Movahed, M. S., Javanmardi, B., Kohandel, M., & Babar, R. (2011). Long-range correlation in cosmic microwave background radiation. *Journal of Statistical Mechanics: Theory and Experiment*, 2011(03), P03007.

Mukhanov, V. F., & Chibisov, G. V. (1981). Quantum fluctuations and a nonsingular universe. *JETP Letters*, 33, 532–535.

Muzy, J. F., Bacry, E., & Arnéodo, A. (1991). Wavelets and multifractal formalism for singular signals: Application to turbulence data. *Physical Review Letters*, 67(25), 3515–3518.

Narcowich, F. J., Petrushev, P., & Ward, J. D. (2006). Localized tight frames on spheres. *SIAM Journal on Mathematical Analysis*, 38(2), 574–594.

Planck Collaboration IV. (2020). Planck 2018 results. IV. Diffuse component separation. *Astronomy & Astrophysics*, 641, A4.

Planck Collaboration VI. (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy & Astrophysics*, 641, A6.

Planck Collaboration VII. (2020). Planck 2018 results. VII. Isotropy and statistics of the CMB. *Astronomy & Astrophysics*, 641, A7.

Planck Collaboration IX. (2020). Planck 2018 results. IX. Constraints on primordial non-Gaussianity. *Astronomy & Astrophysics*, 641, A9.

Tegmark, M., de Oliveira-Costa, A., & Hamilton, A. J. (2003). High resolution foreground cleaned CMB map from WMAP. *Physical Review D*, 68(12), 123523.

Vielva, P., Martínez-González, E., Barreiro, R. B., Sanz, J. L., & Cayón, L. (2004). Detection of non-Gaussianity in the Wilkinson Microwave Anisotropy Probe first-year data using spherical wavelets. *The Astrophysical Journal*, 609(1), 22–34.

Virtanen, P., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods*, 17(3), 261–272.
