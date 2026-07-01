# Fibrillin (FBN1/FBN2/FBN3) expression across developing human and zebrafish heart

## What this is (read before the figures)

This repository does not contain a downloaded spatial transcriptomics count
matrix. In this session, outbound network access to the hosts that hold the
primary data — NCBI/PubMed/PMC, ScienceDirect, bioRxiv, the Human Protein
Atlas, ZFIN, Mendeley Data — was blocked by the sandbox's organization egress
policy (`CONNECT tunnel failed, response 403` at the proxy level, confirmed
with both the WebFetch tool and raw `curl`). Web *search* (snippet-level)
was available and was used to reconstruct what those sources report.

So: `data/*.csv` and `figures/*.png` here are a **qualitative, citation-backed
literature synthesis**, not a re-analysis of the raw Asp et al. 2019 spatial
transcriptomics data, HPA nTPM tables, or ZFIN in-situ records. Every row in
the data tables has a `citation` column. Relative expression is scored on an
ordinal 0-3 scale (undetected / low / moderate / high) inferred from
descriptive statements in the literature (e.g. "highest expression in fetal
tissues," "same temporospatial pattern as FBN1," "expression concentrated in
the AVC by 60-72 hpf") — it is **not** a normalized read count. Treat the
figures as a structured hypothesis/summary to guide a targeted look at the
real datasets, listed in [Getting the primary data yourself](#getting-the-primary-data-yourself) below.

## The three fibrillins, briefly

FBN1, FBN2 and FBN3 encode fibrillins, large glycoproteins that polymerize
into extracellular-matrix microfibrils and scaffold elastic fibers and TGF-β
storage. They differ in temporal pattern:

- **FBN1** — expressed throughout life; the classic Marfan syndrome gene;
  broadly distributed in stromal/ECM-producing cells, smooth muscle, and
  valve interstitial cells (Human Protein Atlas tissue summary; [PMC10806136](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10806136/)).
- **FBN2** — developmentally restricted; in early embryonic organs (skin,
  lung, heart, aorta, CNS anlage, nerves, ganglia) FBN1 and FBN2 "followed the
  same temporospatial pattern of distribution," but FBN2 declines postnatally
  ([PMC10806136](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10806136/)).
- **FBN3** — the most developmentally restricted: "evenly expressed" across
  numerous tissues from the 6th to 12th gestational week, then downregulated
  to low postnatal levels; uniquely high in brain among adult tissues; **has
  no functional ortholog in rodents**, but is present in primates, cow,
  sheep, dog, swine, chick, and zebrafish ([PMID 20970500, Fibrillin-3
  expression in human development](https://pubmed.ncbi.nlm.nih.gov/20970500/)).
  This last point is why zebrafish — not mouse — is the standard model for
  studying FBN3/fbn3 function in vivo.

## Human heart: timeline across developmental stages and layers

Figures: `figures/fig1_human_fibrillin_by_layer.png`,
`figures/fig2_human_endocardium_focus.png`

Stages follow the three time points used by the primary human developmental
heart spatial transcriptomics atlas, **Asp et al. 2019, Cell**, "A
Spatiotemporal Organ-Wide Gene Expression and Cell Atlas of the Developing
Human Heart" ([PMID 31835037](https://pubmed.ncbi.nlm.nih.gov/31835037/),
[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0092867419312826),
raw ST/ISS/scRNA-seq data on [Mendeley Data](https://data.mendeley.com/datasets/dgnysc3zn5/1)),
plus flanking stages from classical cardiac embryology and later single-cell/
spatial extensions (Farah et al. 2024 cardiomyocyte-diversity paper at 6.5-7
PCW; a 2024 multi-omic atlas spanning 4-20 PCW).

Key pattern, **endocardium-focused** (your stated interest):

1. **3.5-4.5 PCW** — linear heart tube / looping. All three fibrillins are low;
   the endocardium is a simple squamous epithelium, not yet making much ECM.
2. **~5 PCW** — endocardial cushions begin forming in the AV canal and
   outflow tract via **endocardial-to-mesenchymal transition (EndMT)**:
   endocardial cells delaminate, invade the cushion, and become
   ECM-secreting mesenchyme ([PMC4760315](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4760315/),
   [ScienceDirect: Endocardial Cushion overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/endocardial-cushion)).
   This is the inflection point where FBN1/2/3 all start rising in the
   endocardial compartment — fibrillin is a product of the post-EndMT
   mesenchyme, not resting endothelium.
3. **6.5-12 PCW** — all three genes peak in endocardium/cushion-derived valve
   mesenchyme. FBN3 in particular sits inside its literature-reported "evenly
   expressed 6th-12th gestational week" window.
4. **>12 PCW → term** — FBN1 stays high (lifelong gene); FBN2 declines
   gradually; **FBN3 drops sharply**, consistent with its reported postnatal
   downregulation.
5. Myocardium and epicardium stay comparatively low for all three genes
   throughout — fibrillins are matrix/mesenchymal-cell products, and
   cardiomyocytes are not a strong fibrillin-producing population per the
   Human Protein Atlas tissue/cell-type data ("membranous and cytoplasmic
   expression in extracellular matrix, stromal cells, smooth muscle cells").

## A newer, higher-resolution atlas: Lázár et al. 2025 (Nature Genetics)

Since the first version of this analysis, the user pointed to
[Lázár et al. 2025, *Nature Genetics*, "Spatiotemporal gene expression and
cellular dynamics of the developing human heart"](https://www.nature.com/articles/s41588-025-02352-6)
(open access on PMC: [PMC12597827](https://pmc.ncbi.nlm.nih.gov/articles/PMC12597827/);
commentary: [Iwamoto-Stohl & Bruneau 2025](https://www.nature.com/articles/s41588-025-02261-8)).
This is the direct successor to Asp et al. 2019 from a related group, and it
is a substantially bigger, later-stage dataset:

- **36 hearts spanning PCW 5.5-14** (Asp et al. 2019 covered ~4.5-9 PCW), so
  it directly fills the 9-14 PCW gap that this analysis' human table had to
  extrapolate.
- 69,114 spatially barcoded spots + 76,991 dissociated cells + targeted in
  situ sequencing (ISS) of a 150-gene panel.
- 23 molecular tissue compartments; 11 primary cell types resolved into 72
  fine-grained cell states, spatially mapped into functional cardiac niches.
- New biology reported: development of the pacemaker-conduction system,
  autonomic innervation, heart valves and the atrial septum, and unexpected
  diversity among cardiac mesenchymal cells.
- Concrete, spatially-validated markers for valve/cushion-related
  populations (relevant context for endocardium/EndMT, even though these are
  not fibrillin genes themselves): endocardial-cushion cells marked by
  **LEF1 + MSX1** (proposed causal role in atrial septal defects), valve
  interstitial cells marked by **APCDD1, LEF1, TMEM132C, ADAMTS19**, and a
  "Valve_MC_1" population marked by **FGF14, HDAC9, PLCXD3**.

**What I could not confirm:** whether FBN1, FBN2 or FBN3 specifically appear
in this paper's 150-gene ISS panel or in its marker-gene tables for
endocardium/valve-mesenchyme cell states. `nature.com`, `pmc.ncbi.nlm.nih.gov`,
`biorxiv.org`, `researchgate.net` and `sciencedirect.com` were all blocked by
this session's egress policy (same `CONNECT tunnel failed, response 403` as
before, re-confirmed for this paper specifically), so I could only work from
search-engine snippets, not the paper's own text, figures, or supplementary
tables. None of the snippets I found named FBN1/2/3 in this paper's marker
lists. **This is a genuine gap, not a "no" answer** — if you (or anyone with
normal browser access) can open the PMC link above, the fastest checks would
be: (1) search the full text for "FBN1", "FBN2", "FBN3", or "fibrillin"; (2)
check Supplementary Table listing the 150 ISS panel genes; (3) check the
marker-gene tables for the endocardial-cushion (LEF1+MSX1) and valve-
mesenchyme cell states. A related, even newer dataset worth the same check is
["MERFISH+, a large-scale, multi-omics spatial technology resolves the
molecular holograms of the 3D human developing heart"](https://www.biorxiv.org/content/10.1101/2025.11.02.686137v1)
(bioRxiv, Nov 2025; >3.1 million cells at subcellular resolution in 3D).

One additional literature point this search surfaced that reinforces the
endocardium/FBN3 link used throughout this analysis: fibrillin-3 protein has
been localized "at the prospective basement membranes in developing
epithelia **and endothelia**," across tissues including heart
([PMID 20970500](https://pubmed.ncbi.nlm.nih.gov/20970500/)) — endocardium
is itself an endothelium, so this is a direct (if not heart-specific)
mechanistic tie-in for why FBN3 shows up there.

## Zebrafish heart: timeline across developmental stages and layers

Figure: `figures/fig3_zebrafish_fibrillin_by_layer.png`

Zebrafish carries three fibrillin genes — **fbn1, fbn2** (renamed from
*fbn2a*), **fbn3** (renamed from *fbn2b*, based on phylogenetics/synteny with
human FBN3) — per the 2025 systematic-disruption study
([bioRxiv 10.1101/2025.06.21.659830](https://www.biorxiv.org/content/10.1101/2025.06.21.659830.full.pdf)).

The best-characterized gene by far, in the endocardium specifically, is
**fbn3 (fbn2b)**:

- **~48 hpf** — endocardial Notch signaling (the pathway fbn3/pku300 act
  through) activates in the AVC and ventricular endocardium.
- **60-72 hpf (2.5-3 dpf)** — Notch signaling concentrates in the AVC;
  fbn3/pku300 are required there for **endocardial cell proliferation,
  adhesion, and tight-junction formation** — i.e., directly for endocardial
  cushion/valve morphogenesis (Wang et al. 2013, *J Cell Sci*,
  [PMC3644139](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3644139/), "Genetic
  interaction between pku300 and fbn2b controls endocardial cell
  proliferation and valve development in zebrafish").
- **4-9 dpf** — in *fbn3⁻/⁻* larvae, this is the window where endocardial
  integrity fails: progressive **endocardial detachment in the atrium**,
  pericardial edema, and in severely affected larvae, death at 6-9 dpf from
  blood-flow obstruction. Milder mutants survive to adulthood with a dilated
  bulbus arteriosus (the zebrafish equivalent of the human aortic root) and
  valvular defects — a Marfan-like cardiovascular phenotype
  ([bioRxiv 10.1101/2025.06.21.659830](https://www.biorxiv.org/content/10.1101/2025.06.21.659830.full.pdf)).
  Notably, **only the fbn3 mutant** among the three single fibrillin mutants
  showed this overt cardiovascular phenotype in that study.
- fbn1 and fbn2 are expressed across the same 1-7 dpf window (established by
  qPCR in the original 2013 paper) but are less well characterized as
  endocardium-specific; they are shown with lower confidence (flatter,
  low-moderate) in the data/figures for that reason.

## Correlating zebrafish stages to human developmental weeks

Figures: `figures/fig4_species_stage_correlation.png`,
`figures/fig5_endocardium_cross_species_overlay.png`
Data: `data/species_stage_correlation.csv`

The correspondence below is **by shared morphogenetic milestone** (same
biological event, not a molecular clock or literal time scaling — zebrafish
hearts form over hours/days, human hearts over weeks):

| Shared process | Zebrafish stage | Human equivalent |
|---|---|---|
| Cardiac progenitor differentiation / cardiac crescent | 12-15 somites (~16 hpf) – 24 hpf | ~3-3.5 PCW |
| Heart tube looping | 24-48 hpf | ~4-5 PCW |
| Endocardial cushion formation / EndMT onset | 48-72 hpf (2-3 dpf) | ~5-6.5 PCW |
| Valve leaflet formation / cushion remodeling, trabeculation | 3-5 dpf | ~6.5-9 PCW |
| Valve/endocardial integrity maturation, chamber septation completion | 5-9 dpf | ~9-12 PCW |
| Post-embryonic / fetal structural maturation | 10 dpf – ~30-90 dpf (juvenile) | ~12 PCW – term/postnatal |

Sources for the milestone timings: Bakkers 2011, *Cardiovasc Res* 91:279,
"Zebrafish as a model to study cardiac development and human cardiac disease"
([PMC3125074](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3125074/)); "From
Stripes to a Beating Heart" review
([PMC7916704](https://pmc.ncbi.nlm.nih.gov/articles/PMC7916704/)); "A
pictorial account of the human embryonic heart between 3.5 and 8 weeks"
([PMC8917235](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8917235/)); "Post-
Embryonic Heart Development and Maturation in Zebrafish"
([PMC4446259](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4446259/)).

When endocardial FBN3 (human) / fbn3 (zebrafish) expression is plotted
against these aligned milestones (fig5), both curves show the same shape:
low before cushion formation, peaking through cushion/valve morphogenesis and
early maturation, then declining once the endocardium's ECM
scaffold/valve architecture is largely built. This is the strongest, most
directly evidenced cross-species link in this analysis, because **fbn3 is
the only one of the three fibrillins with a documented, endocardium-specific
loss-of-function phenotype** (endocardial detachment) in either species —
and because mouse cannot be used for this comparison at all (no functional
Fbn3 ortholog), zebrafish is the primary in vivo model for this gene.

## Caveats

- Values are ordinal, literature-derived estimates, not measured expression;
  treat trends (rising/falling, relative ranking of genes/layers) as more
  reliable than exact levels.
- FBN2/FBN3 data points for myocardium/epicardium in both species are lower-
  confidence extrapolations (fibrillins are broadly ECM/mesenchymal-cell
  products; layer-specific reports are sparser than for endocardium).
- The human-zebrafish stage correspondence is a standard comparative-
  embryology device (shared morphogenetic milestones), not a validated
  molecular timeline alignment.
- FBN1/FBN2 in zebrafish endocardium specifically (as opposed to whole
  embryo) are less well documented in the literature surfaced here than
  fbn3; corresponding figure lines are drawn flatter/lower-confidence.

## Getting the primary data yourself

If you want actual counts rather than this literature synthesis:

### Lázár et al. 2025 (Nature Genetics) — the recommended source for PCW 5.5-14

The corresponding authors have deposited the full processed dataset. Per the
paper's Data Availability statement (reproduced here as given by the user,
since this session cannot browse to it directly):

- **Mendeley Data, part 1**: Cell Ranger output, Space Ranger output,
  metadata, processed ISS data, supplementary figures/tables, and main RDS
  objects — DOI [10.17632/fhtb99mdzd.1](https://doi.org/10.17632/fhtb99mdzd.1)
  / <https://data.mendeley.com/datasets/fhtb99mdzd/1>
- **Mendeley Data, part 2**: DOI [10.17632/w65jtfsvpr.1](https://doi.org/10.17632/w65jtfsvpr.1)
  / <https://data.mendeley.com/datasets/w65jtfsvpr/1>
- **Interactive browser** (no download needed to check FBN1/2/3 by eye):
  <https://hdcaheart.serve.scilifelab.se/web/index.html> — lets you browse
  Visium, scRNA-seq, and ISS gene expression, clustering, and other results
  directly; the site has its own usage instructions.
- **Raw sequencing** (controlled access, formal request required): single-cell
  at EGA study [EGAS50000001029](https://ega-archive.org/studies/EGAS50000001029),
  spatial transcriptomics at EGA study
  [EGAS50000001122](https://ega-archive.org/studies/EGAS50000001122). Raw ISS
  images are available from the corresponding authors on reasonable request
  (not deposited, per the paper).

For a direct FBN1/FBN2/FBN3-in-endocardium answer, the **interactive
browser is the fastest path** — search each gene, filter/select the
endocardium or endocardial-cushion/valve-mesenchyme cell states, and read
off expression across the PCW 5.5-14 samples.

### Asp et al. 2019 (Cell) — PCW ~4.5-9

Raw ST/ISS/scRNA-seq data and processed expression matrices —
[Mendeley Data (dgnysc3zn5)](https://data.mendeley.com/datasets/dgnysc3zn5/1)
and the paper's [online spatial viewer](https://www.sciencedirect.com/science/article/pii/S0092867419312826).

### Other sources used in this analysis

- Human Protein Atlas single-cell/tissue pages for exact nTPM values:
  [FBN1](https://www.proteinatlas.org/ENSG00000166147-FBN1/single+cell+type),
  [FBN2](https://proteinatlas.org/ENSG00000138829-FBN2/single+cell+type),
  [FBN3](https://www.proteinatlas.org/ENSG00000142449-FBN3).
- **Zebrafish**: [ZFIN](https://zfin.org/) gene pages for `fbn1`, `fbn2`,
  `fbn3` (search current nomenclature — `fbn3` was formerly `fbn2b`) have
  curated in-situ expression records by stage. The 2025 Marfan-model paper's
  RNA-seq data is deposited as [GEO GSE300393](https://www.omicsdi.org/dataset/geo/GSE300393).

### Why none of this is already pulled into `data/*.csv`

This session's outbound network access is governed by an organization
egress policy that explicitly denies every one of the above hosts —
`data.mendeley.com`, `doi.org`, `hdcaheart.serve.scilifelab.se`,
`ega-archive.org`, plus `ncbi.nlm.nih.gov`, `sciencedirect.com`,
`biorxiv.org`, and `proteinatlas.org` from earlier checks. Each was
re-confirmed via the proxy's own status log as an explicit
`connect_rejected` / "gateway answered 403 to CONNECT (policy denial)",
not a transient network error — so retrying or working around it isn't
appropriate here.

**If you (or anyone with normal, unrestricted network access) can open the
interactive browser or download the Mendeley RDS objects and pull actual
FBN1/FBN2/FBN3 values by cell state and stage** — even just pasted numbers,
a screenshot of the browser's expression view, or an exported CSV — paste
them into the conversation and this analysis can be redone with real
measured data: `data/human_fibrillin_expression.csv` swapped for real
values and `scripts/plot_fibrillin_timelines.py` re-run unchanged to
regenerate all figures.

## Reproducing the figures

```
pip install matplotlib pandas numpy
python3 scripts/plot_fibrillin_timelines.py
```
