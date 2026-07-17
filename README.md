# SpatialHumanHeart

Spatial transcriptomics-informed analysis of fibrillin (FBN1/FBN2/FBN3) and
CDH5/VE-cadherin expression across developing human heart layers
(endocardium, myocardium, epicardium), correlated to zebrafish
(fbn1/fbn2/fbn3, cdh5) heart developmental stages.

- **[ANALYSIS.md](ANALYSIS.md)** — full write-up, citations, and important
  caveats about data provenance (read this first).
- `data/` — human and zebrafish expression tables (qualitative,
  literature-derived, fully cited) and the cross-species stage-correlation
  table.
- `scripts/plot_fibrillin_timelines.py` — regenerates all figures from the
  CSVs in `data/`.
- `figures/` — timeline and layer-expression plots, including an
  endocardium-focused human/zebrafish overlay.
