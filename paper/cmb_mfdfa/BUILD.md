# CMB MFDFA — build

No pdflatex path (the md uses Unicode math). Built with pandoc + WeasyPrint (S342, v2):

    pandoc paper/cmb_mfdfa/cmb-mfdfa.md -s --pdf-engine=weasyprint --css paper/cmb_mfdfa/cmb.css \
      --metadata pagetitle="Scale-Dependent Multifractal Structure in the Planck 2018 CMB" -o tmp/zen-cmb/cmb-mfdfa-paper.pdf

Zenodo record also carries `cmb_proper_mfdfa.py` and the six figures: re-version with
`ZENODO_KEEP_OTHER_FILES=1 ZENODO_CONCEPT_DOI=10.5281/zenodo.20306784 bash scripts/zenodo-upload.sh tmp/zen-cmb/cmb-mfdfa-paper.pdf`.
