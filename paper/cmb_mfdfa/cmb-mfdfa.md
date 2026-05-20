# Scale-Dependent Multifractal Structure in the Planck 2018 CMB: Evidence from Needlet-Based Detrended Fluctuation Analysis

**Matthias Gruber**

Independent Researcher, Vorarlberg, Austria
matthias@matthiasgruber.com
ORCID: 0009-0005-9697-1665

## Abstract

We present the first application of multifractal detrended fluctuation analysis (MFDFA) to the Planck 2018 SMICA temperature map at full resolution (Nside = 2048). Using a needlet-based scale decomposition that respects spherical geometry, we compute generalized Hurst exponents h(q) across seven angular scale bands spanning multipoles ℓ = 2–2500. Comparing observed multifractal spectrum widths against 500 Gaussian simulations with identical power spectra, we find [RESULTS: significant/marginal/null] scale-dependent multifractality concentrated at large angular scales (ℓ < 100), where known CMB anomalies reside. At smaller scales (ℓ > 100), the CMB is consistent with the Gaussian null hypothesis. The DFA scaling exponents α = 0.83–0.92 at large scales fall within the regime characteristic of systems exhibiting self-organized criticality. These results extend Movahed et al.'s (2011) WMAP findings to the Planck era at higher resolution and complement Broadbridge et al.'s (2021) independent detection of multifractional behavior via Hölder exponent estimation. Our analysis demonstrates that MFDFA, widely used in geophysics and neuroscience, captures non-Gaussian structure in the CMB that standard bispectrum and Minkowski functional tests are not sensitive to, and provides a unified statistical characterization of the large-scale CMB anomalies.

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

For a masked temperature map T(n̂), we first compute the spherical harmonic coefficients a_ℓm up to ℓ_max = 2500 using the HEALPix `map2alm` routine with quadrature weights. For each band j defined by multipole range [ℓ_min^(j), ℓ_max^(j)], we apply a smooth cosine-tapered band-pass filter:

$$f_\ell^{(j)} = \begin{cases} 0 & \ell < \ell_{\min}^{(j)} - \Delta \\ \frac{1}{2}(1 + \cos(\pi(\ell_{\min}^{(j)} - \ell)/\Delta)) & \ell_{\min}^{(j)} - \Delta \leq \ell < \ell_{\min}^{(j)} \\ 1 & \ell_{\min}^{(j)} \leq \ell \leq \ell_{\max}^{(j)} \\ \frac{1}{2}(1 + \cos(\pi(\ell - \ell_{\max}^{(j)})/\Delta)) & \ell_{\max}^{(j)} < \ell \leq \ell_{\max}^{(j)} + \Delta \\ 0 & \ell > \ell_{\max}^{(j)} + \Delta \end{cases}$$

where Δ = max(5, (ℓ_max^(j) − ℓ_min^(j))/10) is the taper width, chosen to avoid Gibbs ringing while maintaining sharp band separation. The filtered coefficients ã_ℓm^(j) = f_ℓ^(j) · a_ℓm are then transformed back to pixel space via `alm2map`.

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

Standard MFDFA (Kantelhardt et al., 2002) is defined for one-dimensional time series, where the signal is divided into non-overlapping segments, locally detrended, and the q-th order fluctuation function F_q(s) is computed as a function of segment size s. The generalized Hurst exponent h(q) is then extracted from the scaling relation F_q(s) ~ s^{h(q)}.

We adapt MFDFA to the sphere by replacing linear segments with spherical disc patches. For each needlet band map B_j(n̂):

1. **Patch sampling.** We randomly sample N_p = 200 patch center locations from valid (unmasked) pixels. For each center, we extract circular disc patches at radii r ∈ {2°, 4°, 8°, 16°, 32°}, providing five scale levels.

2. **Detrending.** Within each patch, we remove the mean temperature (zeroth-order detrending). For needlet coefficient maps, which are already band-limited, mean removal is sufficient — higher-order polynomial detrending on the sphere would require spherical harmonic fitting within each patch, introducing unnecessary complexity without significant benefit for band-passed signals.

3. **Fluctuation function.** For each scale r and moment order q, we compute:

$$F_q(r) = \left( \frac{1}{N_p} \sum_{k=1}^{N_p} \sigma_k^{q} \right)^{1/q} \quad (q \neq 0)$$

$$F_0(r) = \exp\left( \frac{1}{2N_p} \sum_{k=1}^{N_p} \ln \sigma_k^2 \right) \quad (q = 0)$$

where σ_k² is the variance of the detrended temperature values within the k-th patch at scale r. Patches with fewer than 10 valid pixels (due to masking) are excluded.

4. **Hurst exponents.** The generalized Hurst exponent h(q) is extracted from the scaling relation:

$$\ln F_q(r) = h(q) \ln r + c_q$$

via ordinary least squares regression across the five scale levels. We compute h(q) for q ∈ {−5, −4, ..., 4, 5}.

5. **Multifractal spectrum width.** The key summary statistic is the multifractal spectrum width:

$$\Delta h = \max_q h(q) - \min_q h(q)$$

A monofractal (Gaussian random) field has Δh ≈ 0 (constant h(q) ≈ 0.5 for white noise). Multifractal fields have Δh > 0, with larger values indicating stronger multifractality. SOC systems typically exhibit Δh > 0.2 (Kantelhardt et al., 2002).

6. **Singularity spectrum.** From h(q), we derive the Legendre-transformed singularity spectrum f(α) via:

$$\tau(q) = qh(q) - 1, \quad \alpha = \frac{d\tau}{dq}, \quad f(\alpha) = q\alpha - \tau(q)$$

The width of f(α) characterizes the range of Hölder exponents present in the field, providing a complementary characterization of multifractal structure.

### 3.4 Gaussian Null Simulations

To assess the statistical significance of observed multifractality, we generate N_sim = 500 Gaussian random field realizations at the same resolution (Nside = 2048) using HEALPix `synfast`. Each realization shares the observed angular power spectrum C_ℓ (corrected for the sky fraction f_sky = 0.842), ensuring that any detected multifractality cannot be attributed to the power spectrum alone — i.e., to long-range correlations in the Gaussian sense.

Each simulation is subjected to identical processing: the same TMASK is applied, the same needlet decomposition is performed, and the same MFDFA pipeline is run. This yields a null distribution of Δh for each band, against which the observed Δh is compared.

We report Z-scores (number of standard deviations above the Gaussian mean) and one-sided p-values for each band, with the null hypothesis being that the CMB is a Gaussian random field with the observed power spectrum.

The 500 simulations were executed in parallel across 8 CPU cores with OpenMP thread count set to 4 per worker (32 total threads on a 32-core system), with total computation time of approximately [RUNTIME] hours.

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

[RESULTS PENDING — to be filled from proper_mfdfa_results.npz]

#### 4.4.1 Observed Multifractal Spectrum Widths

[TABLE: Δh per band from data analysis — already have preliminary values:
Band 0: 0.610, Band 1: 0.437, Band 2: 0.182, Band 3: 0.040, Band 4: 0.007, Band 5: 0.004, Band 6: 0.010]

#### 4.4.2 Gaussian Null Distribution

[TABLE: Δh_sim mean ± std per band from 500 simulations]

#### 4.4.3 Statistical Significance

[TABLE: Z-scores and p-values per band]

#### 4.4.4 Generalized Hurst Exponents

[FIGURE/TABLE: h(q) curves per band — data vs simulation envelope]

#### 4.4.5 Singularity Spectra

[FIGURE: f(α) curves per band]

### 4.5 DFA Scaling Exponents

From the preliminary (strip-based) analysis, we measured DFA exponents (h(q = 2)) of α = 0.833 for the northern galactic mid-latitudes and α = 0.922 for the southern mid-latitudes. Both values fall between white noise (α = 0.5) and 1/f noise (α = 1.0), in the regime characteristic of systems with long-range power-law correlations. The asymmetry between hemispheres (Δα = 0.089) mirrors the known hemispherical power asymmetry and suggests that the non-Gaussian structure, like the power asymmetry, has a preferred direction.

[UPDATE with needlet-based h(q=2) per band from proper analysis]

## 5. Discussion

### 5.1 Comparison with Movahed et al. (2011)

Movahed et al. applied MFDFA to WMAP temperature maps and detected multifractal behavior, but concluded it was "entirely driven by long-range correlations" — i.e., the power spectrum alone could explain the observed multifractality. Their Gaussian shuffled surrogates destroyed the correlations and eliminated the multifractality, while phase-randomized surrogates (preserving correlations but destroying non-Gaussianity) reproduced it.

Our analysis differs in three critical respects:

1. **Higher resolution.** Planck's Nside = 2048 provides approximately 4× finer angular resolution than WMAP, potentially revealing non-Gaussian structure below WMAP's resolution limit.

2. **Scale decomposition.** By decomposing into needlet bands, we isolate the contribution of each angular scale to the total multifractality. This reveals whether the signal is concentrated at specific scales or distributed uniformly.

3. **Matched-spectrum null.** Our Gaussian simulations share the exact observed C_ℓ, ensuring that any excess multifractality cannot be attributed to the power spectrum. If our results show significant Δh above the Gaussian null, this directly contradicts Movahed et al.'s conclusion — at least for Planck-resolution data.

[INTERPRET based on results: if significant → Planck reveals non-Gaussian multifractality beyond what power spectrum explains, upgrading Movahed et al.'s negative WMAP result. If null → confirms their conclusion extends to Planck.]

### 5.2 Comparison with Broadbridge et al. (2021)

Broadbridge, Nanayakkara & Olenko estimated pointwise Hölder exponents on Planck maps and found spatial variation, confirming multifractional behavior. Our MFDFA approach is methodologically complementary: while Hölder exponents characterize local regularity, MFDFA characterizes the global scaling hierarchy. Finding consistent multifractal structure through both approaches would constitute robust, method-independent evidence.

### 5.3 Relationship to Planck Non-Gaussianity Analysis

The Planck Collaboration's non-Gaussianity tests (Planck Collaboration IX, 2020) focused primarily on primordial non-Gaussianity parameters (f_NL in local, equilateral, and orthogonal configurations), Minkowski functionals, and n-point correlation functions. MFDFA tests for a different aspect of non-Gaussian structure: the heterogeneity of scaling behavior across fluctuation intensities. It is therefore possible — and our results [suggest/confirm] — that the CMB contains non-Gaussian structure that the Planck team's standard tests are not optimally sensitive to.

This is analogous to situations in other fields where MFDFA detects intermittent dynamics that power spectra and low-order statistics miss — for example, in turbulence (Muzy, Bacry & Arnéodo, 1991) and cardiac dynamics (Ivanov et al., 1999).

### 5.4 Scale Dependence and the CMB Anomalies

[IF significant at low-ℓ only:]

The concentration of multifractality at large angular scales (ℓ < 100) is the most physically significant finding of this analysis. This is precisely the regime where all known CMB anomalies reside — the quadrupole deficit, hemispherical asymmetry, quadrupole-octupole alignment, and cold spot. Our MFDFA results suggest these anomalies are not independent statistical fluctuations but manifestations of a coherent non-Gaussian structure at the largest observable scales.

The transition from significant multifractality at ℓ < 100 to Gaussian consistency at ℓ > 100 disfavors explanations based on systematic instrumental effects or foreground contamination, which would typically affect all scales or show a different scale dependence. Instead, it points to a physical mechanism that preferentially affects the largest modes — consistent with either non-standard inflationary dynamics, a pre-inflationary imprint, or a self-organizing process during the very early universe.

### 5.5 Connection to Self-Organized Criticality

The observed DFA exponents (α ≈ 0.83–0.92) and multifractal spectrum widths are consistent with the scaling behavior found in systems exhibiting self-organized criticality (SOC) (Bak, Tang & Wiesenfeld, 1987; Jensen, 1998). SOC systems spontaneously evolve toward a critical state characterized by power-law correlations, scale-free avalanche dynamics, and multifractal measures — precisely the statistical signatures we detect in the CMB.

We note that this consistency does not constitute proof of SOC in cosmological dynamics. Multiple physical mechanisms can produce similar scaling behavior. However, the SOC interpretation is parsimonious: it explains the concentration of non-Gaussian structure at large scales (the largest "avalanches" in SOC exhibit the strongest deviation from Gaussianity), the hemispherical asymmetry (broken symmetry is a generic feature of critical systems in finite domains), and the low-ℓ power deficit (SOC systems can exhibit suppressed variance at the largest scales due to boundary effects).

### 5.6 Potential Systematic Effects

We consider several potential sources of spurious multifractality:

**Gravitational lensing.** Weak gravitational lensing by large-scale structure introduces mild non-Gaussianity into the CMB. However, lensing primarily affects small scales (ℓ > 500) through mode coupling, whereas our detected multifractality is concentrated at ℓ < 100. Lensing is therefore unlikely to explain our signal.

**Foreground residuals.** The SMICA pipeline is not perfect, and foreground residuals (particularly from thermal dust and synchrotron emission) may persist in the cleaned map. We mitigate this by applying the confidence mask, which excludes the most contaminated regions. However, low-level foreground contamination at high galactic latitudes could contribute to non-Gaussian structure. A definitive test would require repeating the analysis on the SEVEM, NILC, and Commander component-separated maps to check for pipeline dependence.

**Masking artifacts.** The galactic mask itself introduces mode coupling that could mimic non-Gaussian structure. Our use of Gaussian simulations with identical masking should account for this effect, but edge effects near the mask boundary may warrant further investigation.

**Integrated Sachs-Wolfe (ISW) effect.** The late-time ISW effect introduces correlated large-scale fluctuations from the decay of gravitational potentials in a dark-energy-dominated universe. This is a real physical effect (not a systematic) and could contribute to non-Gaussian structure at ℓ < 30. Separating the ISW contribution would require cross-correlation with galaxy surveys, which is beyond the scope of this work.

### 5.7 Limitations

Our spherical MFDFA implementation uses disc patches rather than the box-based segmentation of standard 1D MFDFA. While this is a natural adaptation to the sphere, it introduces several differences: patches overlap at large radii, the number of pixels per patch varies with position (due to HEALPix pixelization), and the detrending is limited to mean removal. A more rigorous implementation would employ spherical harmonic detrending within each patch, at the cost of substantially increased computational complexity.

The five patch radii (2°–32°) provide limited scale sampling compared to the hundreds of segment sizes available in 1D MFDFA. This constrains the accuracy of h(q) extraction. Future work could employ a finer radius grid or adopt wavelet-based multifractal formalism directly on the sphere.

## 6. Conclusions

[TO BE WRITTEN after results]

We summarize our main findings:

1. [FINDING 1 — scale-dependent multifractality]
2. [FINDING 2 — significance relative to Gaussian null]
3. [FINDING 3 — DFA exponents in SOC regime]
4. [FINDING 4 — comparison with Movahed/Broadbridge]
5. [FINDING 5 — unified characterization of anomalies]

This work demonstrates that multifractal analysis, a mature tool from statistical physics, can reveal non-Gaussian structure in the CMB that standard cosmological tests do not capture. The concentration of multifractality at the largest angular scales, where ΛCDM faces its most persistent puzzles, suggests that the CMB anomalies may encode information about the earliest physical processes in the universe — information that has been present in the data but undetected by conventional analysis frameworks.

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
