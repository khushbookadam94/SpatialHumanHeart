"""
Generate timeline / layer-expression figures for FBN1, FBN2, FBN3 in the
developing human heart, the developing zebrafish heart, and a cross-species
correlation of developmental stages.

Inputs (data/):
  human_fibrillin_expression.csv
  zebrafish_fibrillin_expression.csv
  species_stage_correlation.csv

All "relative_expression_0to3" values are qualitative estimates synthesized
from published descriptions (see citation column and ANALYSIS.md) -- this
session had no network path to download the raw Asp et al. 2019 spatial
transcriptomics counts, ZFIN in-situ records, or Human Protein Atlas nTPM
tables (organization egress policy blocks those hosts). Treat plotted values
as an illustrative, citation-backed summary of the literature, not measured
expression.

Outputs (figures/):
  fig1_human_fibrillin_by_layer.png
  fig2_human_endocardium_focus.png
  fig3_zebrafish_fibrillin_by_layer.png
  fig4_species_stage_correlation.png
  fig5_endocardium_cross_species_overlay.png
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
FIGS = os.path.join(BASE, "figures")
os.makedirs(FIGS, exist_ok=True)

human = pd.read_csv(os.path.join(DATA, "human_fibrillin_expression.csv"))
zfish = pd.read_csv(os.path.join(DATA, "zebrafish_fibrillin_expression.csv"))
corr = pd.read_csv(os.path.join(DATA, "species_stage_correlation.csv"))

LAYER_COLORS = {"Endocardium": "#c0392b", "Myocardium": "#2980b9", "Epicardium": "#27ae60"}
GENE_COLORS = {"FBN1": "#7d3c98", "FBN2": "#d68910", "FBN3": "#c0392b",
               "fbn1": "#7d3c98", "fbn2": "#d68910", "fbn3": "#c0392b"}

CAVEAT = ("Expression levels are qualitative, literature-derived estimates (0=undetected .. 3=high),\n"
          "not measured counts -- see ANALYSIS.md for full citations and caveats.")

# ---------------------------------------------------------------------------
# Figure 1: Human heart -- one panel per gene, lines = heart layer, x = PCW
# ---------------------------------------------------------------------------
genes = ["FBN1", "FBN2", "FBN3"]
stages = sorted(human["stage_pcw"].unique())

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for ax, gene in zip(axes, genes):
    sub = human[human["gene"] == gene]
    for layer in ["Endocardium", "Myocardium", "Epicardium"]:
        ls = sub[sub["heart_layer"] == layer].sort_values("stage_pcw")
        lw = 3.5 if layer == "Endocardium" else 1.8
        alpha = 1.0 if layer == "Endocardium" else 0.75
        ax.plot(ls["stage_pcw"], ls["relative_expression_0to3"], marker="o",
                lw=lw, alpha=alpha, color=LAYER_COLORS[layer], label=layer)
    ax.set_title(gene, fontsize=13, fontweight="bold")
    ax.set_xlabel("Post-conception week (PCW)")
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(["undetected", "low", "moderate", "high"])
    ax.axvspan(6, 12, color="grey", alpha=0.08)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("Relative expression")
axes[0].legend(loc="lower right", fontsize=9, framealpha=0.9)
fig.suptitle("Fibrillin (FBN1/2/3) expression across developing human heart layers\n"
             "(shaded band = 6-12 PCW window of broad FBN2/FBN3 fetal expression)",
             fontsize=13)
fig.text(0.5, -0.02, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.02, 1, 0.94])
fig.savefig(os.path.join(FIGS, "fig1_human_fibrillin_by_layer.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 2: Human endocardium focus -- all 3 genes overlaid, endocardium only
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.5, 6))
endo = human[human["heart_layer"] == "Endocardium"]
for gene in genes:
    ls = endo[endo["gene"] == gene].sort_values("stage_pcw")
    ax.plot(ls["stage_pcw"], ls["relative_expression_0to3"], marker="o", lw=3,
            color=GENE_COLORS[gene], label=gene)
ax.axvspan(5, 6.5, color="#f1c40f", alpha=0.15)
ax.text(5.1, 3.75, "EndMT / cushion\nformation onset", fontsize=8, va="top")
ax.axvspan(6, 12, color="grey", alpha=0.08)
ax.text(7.5, -0.55, "FBN2/FBN3 broad fetal window (6-12 PCW)", fontsize=8, color="dimgrey")
ax.set_xlabel("Post-conception week (PCW)")
ax.set_ylabel("Relative expression in endocardium")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylim(-0.4, 4.0)
ax.set_title("FBN1 vs FBN2 vs FBN3 in the endocardium across human heart development", fontsize=12)
ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.55), framealpha=0.95)
ax.grid(alpha=0.3)
fig.text(0.5, -0.05, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.02, 1, 1])
fig.savefig(os.path.join(FIGS, "fig2_human_endocardium_focus.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 3: Zebrafish heart -- one panel per gene, lines = heart layer, x = hpf/dpf
# ---------------------------------------------------------------------------
zgenes = ["fbn1", "fbn2", "fbn3"]
zfish_stage_order = sorted(zfish["stage_hpf"].unique())
stage_labels = (zfish.drop_duplicates("stage_hpf").set_index("stage_hpf")["stage_label"]
                .to_dict())

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for ax, gene in zip(axes, zgenes):
    sub = zfish[zfish["gene"] == gene]
    for layer in ["Endocardium", "Myocardium"]:
        ls = sub[sub["heart_layer"] == layer].sort_values("stage_hpf")
        lw = 3.5 if layer == "Endocardium" else 1.8
        alpha = 1.0 if layer == "Endocardium" else 0.75
        ax.plot(ls["stage_hpf"], ls["relative_expression_0to3"], marker="o",
                lw=lw, alpha=alpha, color=LAYER_COLORS[layer], label=layer)
    ax.set_title(gene, fontsize=13, fontweight="bold", style="italic")
    ax.set_xticks(zfish_stage_order)
    ax.set_xticklabels([stage_labels[s] for s in zfish_stage_order], rotation=45, ha="right")
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(["undetected", "low", "moderate", "high"])
    ax.axvspan(48, 168, color="grey", alpha=0.08)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("Relative expression")
axes[0].legend(loc="lower right", fontsize=9, framealpha=0.9)
fig.suptitle("Fibrillin (fbn1/fbn2/fbn3) expression across developing zebrafish heart layers\n"
             "(shaded band = 48 hpf-7 dpf endocardial-cushion / valve morphogenesis window)",
             fontsize=13)
fig.text(0.5, -0.05, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.03, 1, 0.90])
fig.savefig(os.path.join(FIGS, "fig3_zebrafish_fibrillin_by_layer.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 4: Species stage correlation timeline (dumbbell / connector chart)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5))
n = len(corr)
y = list(range(n, 0, -1))
for yi, row in zip(y, corr.itertuples()):
    ax.plot([0, 1], [yi, yi], color="lightgrey", lw=2, zorder=1)
    ax.scatter([0], [yi], color="#2471a3", s=140, zorder=2)
    ax.scatter([1], [yi], color="#c0392b", s=140, zorder=2)
    ax.text(-0.03, yi, row.zebrafish_stage, ha="right", va="center", fontsize=9)
    ax.text(1.03, yi, row.human_pcw_equivalent, ha="left", va="center", fontsize=9)
    ax.text(0.5, yi + 0.22, row.shared_process, ha="center", va="bottom",
            fontsize=8.5, style="italic", color="dimgrey")
ax.set_xlim(-0.9, 1.9)
ax.set_ylim(0.3, n + 1)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Zebrafish stage", "Human equivalent (PCW)"], fontsize=11, fontweight="bold")
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title("Correlating zebrafish heart developmental stages to human post-conception weeks\n"
             "(approximate correspondence by shared morphogenetic milestone, not a molecular clock)",
             fontsize=12)
fig.text(0.5, 0.0, "See data/species_stage_correlation.csv for citations per row.",
         ha="center", fontsize=8, style="italic")
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig4_species_stage_correlation.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 5: Endocardium-focused cross-species overlay, aligned by milestone
# ---------------------------------------------------------------------------
milestone_order = [
    "Cardiac progenitor differentiation / cardiac crescent",
    "Heart tube looping",
    "Endocardial cushion formation / EndMT onset",
    "Valve leaflet formation / cushion remodeling, trabeculation",
    "Valve/endocardial integrity maturation, chamber septation completion",
    "Post-embryonic / fetal structural maturation",
]
x_pos = {m: i for i, m in enumerate(milestone_order)}

# Map each human stage_pcw to nearest milestone bucket for FBN3 endocardium curve
human_milestone_map = {3.5: 0, 4.5: 1, 5: 2, 6.5: 3, 9: 4, 12: 4, 20: 5, 40: 5}
zfish_milestone_map = {24: 0, 48: 1, 72: 2, 120: 3, 168: 4, 216: 4, 720: 5}

h_fbn3 = human[(human["gene"] == "FBN3") & (human["heart_layer"] == "Endocardium")].copy()
h_fbn3["milestone_x"] = h_fbn3["stage_pcw"].map(human_milestone_map)
h_fbn3 = h_fbn3.groupby("milestone_x")["relative_expression_0to3"].max().reset_index()

z_fbn3 = zfish[(zfish["gene"] == "fbn3") & (zfish["heart_layer"] == "Endocardium")].copy()
z_fbn3["milestone_x"] = z_fbn3["stage_hpf"].map(zfish_milestone_map)
z_fbn3 = z_fbn3.groupby("milestone_x")["relative_expression_0to3"].max().reset_index()

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(h_fbn3["milestone_x"], h_fbn3["relative_expression_0to3"], marker="o", lw=3,
        color="#c0392b", label="Human FBN3 (endocardium)")
ax.plot(z_fbn3["milestone_x"], z_fbn3["relative_expression_0to3"], marker="s", lw=3,
        ls="--", color="#1abc9c", label="Zebrafish fbn3 (endocardium)")
ax.set_xticks(range(len(milestone_order)))
ax.set_xticklabels([m.replace(" / ", "/\n") for m in milestone_order], fontsize=8, rotation=15, ha="right")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylabel("Relative expression in endocardium")
ax.set_title("Endocardial FBN3/fbn3 expression aligned across shared cardiac morphogenetic\n"
             "milestones in human and zebrafish (no mouse ortholog exists for FBN3)", fontsize=12)
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
fig.text(0.5, -0.08, CAVEAT + "\nMilestone alignment per data/species_stage_correlation.csv.",
         ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(FIGS, "fig5_endocardium_cross_species_overlay.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

print("Wrote figures to", FIGS)
for f in sorted(os.listdir(FIGS)):
    print(" -", f)
