"""
Generate timeline / layer-expression figures for CDH5 (VE-cadherin) in the
developing human heart, the developing zebrafish heart (cdh5), and a
cross-species endocardium overlay -- same structure as
plot_fibrillin_timelines.py, applied to the endothelial/endocardial adherens-
junction gene instead of the fibrillins.

Inputs (data/):
  human_cdh5_expression.csv
  zebrafish_cdh5_expression.csv
  species_stage_correlation.csv          (reused from the fibrillin analysis)
  human_fibrillin_expression.csv         (for the contrast panel only)
  zebrafish_fibrillin_expression.csv     (for the contrast panel only)

Same caveat as the fibrillin analysis: values are qualitative, literature-
derived estimates (0=undetected .. 3=high), not measured counts. See
ANALYSIS.md for citations and caveats.

Outputs (figures/):
  fig6_human_cdh5_by_layer.png
  fig7_zebrafish_cdh5_by_layer.png
  fig8_endocardium_cdh5_cross_species_overlay.png
  fig9_endocardium_cdh5_vs_fbn_contrast.png
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
FIGS = os.path.join(BASE, "figures")
os.makedirs(FIGS, exist_ok=True)

human = pd.read_csv(os.path.join(DATA, "human_cdh5_expression.csv"))
zfish = pd.read_csv(os.path.join(DATA, "zebrafish_cdh5_expression.csv"))
human_fbn = pd.read_csv(os.path.join(DATA, "human_fibrillin_expression.csv"))
zfish_fbn = pd.read_csv(os.path.join(DATA, "zebrafish_fibrillin_expression.csv"))

LAYER_COLORS = {"Endocardium": "#c0392b", "Myocardium": "#2980b9", "Epicardium": "#27ae60"}
CAVEAT = ("Expression levels are qualitative, literature-derived estimates (0=undetected .. 3=high),\n"
          "not measured counts -- see ANALYSIS.md for full citations and caveats.")

# ---------------------------------------------------------------------------
# Figure 6: Human CDH5 -- one panel, lines = heart layer, x = PCW
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5.5))
for layer in ["Endocardium", "Myocardium", "Epicardium"]:
    ls = human[human["heart_layer"] == layer].sort_values("stage_pcw")
    lw = 3.5 if layer == "Endocardium" else 1.8
    alpha = 1.0 if layer == "Endocardium" else 0.75
    ax.plot(ls["stage_pcw"], ls["relative_expression_0to3"], marker="o",
            lw=lw, alpha=alpha, color=LAYER_COLORS[layer], label=layer)
ax.axvspan(5, 6.5, color="#f1c40f", alpha=0.15)
ax.text(5.1, 0.15, "EndMT dip\n(Snail-repressed\nin cushion subset)", fontsize=7.5)
ax.set_xlabel("Post-conception week (PCW)")
ax.set_ylabel("Relative expression")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylim(-0.4, 3.4)
ax.set_title("CDH5 (VE-cadherin) across developing human heart layers\n"
             "(constitutive endothelial marker -- contrast with fibrillin's late rise)", fontsize=12)
ax.legend(loc="center right", framealpha=0.95)
ax.grid(alpha=0.3)
fig.text(0.5, -0.05, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.02, 1, 1])
fig.savefig(os.path.join(FIGS, "fig6_human_cdh5_by_layer.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 7: Zebrafish cdh5 -- one panel, lines = heart layer, x = hpf/dpf
# ---------------------------------------------------------------------------
zfish_stage_order = sorted(zfish["stage_hpf"].unique())
stage_labels = zfish.drop_duplicates("stage_hpf").set_index("stage_hpf")["stage_label"].to_dict()

fig, ax = plt.subplots(figsize=(8, 5.5))
for layer in ["Endocardium", "Myocardium"]:
    ls = zfish[zfish["heart_layer"] == layer].sort_values("stage_hpf")
    lw = 3.5 if layer == "Endocardium" else 1.8
    alpha = 1.0 if layer == "Endocardium" else 0.75
    ax.plot(ls["stage_hpf"], ls["relative_expression_0to3"], marker="o",
            lw=lw, alpha=alpha, color=LAYER_COLORS[layer], label=layer)
ax.axvspan(48, 120, color="#f1c40f", alpha=0.15)
ax.text(50, 0.15, "AVC-restricted\ndownregulation\n(60-72 hpf)", fontsize=7.5)
ax.set_xticks(zfish_stage_order)
ax.set_xticklabels([stage_labels[s] for s in zfish_stage_order], rotation=45, ha="right")
ax.set_ylabel("Relative expression")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylim(-0.4, 3.4)
ax.set_title("cdh5 (VE-cadherin) across developing zebrafish heart layers", fontsize=12)
ax.legend(loc="center right", framealpha=0.95)
ax.grid(alpha=0.3)
fig.text(0.5, -0.08, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.05, 1, 1])
fig.savefig(os.path.join(FIGS, "fig7_zebrafish_cdh5_by_layer.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 8: Endocardium-focused cross-species overlay, aligned by milestone
# ---------------------------------------------------------------------------
milestone_order = [
    "Cardiac progenitor differentiation / cardiac crescent",
    "Heart tube looping",
    "Endocardial cushion formation / EndMT onset",
    "Valve leaflet formation / cushion remodeling, trabeculation",
    "Valve/endocardial integrity maturation, chamber septation completion",
    "Post-embryonic / fetal structural maturation",
]
human_milestone_map = {3.5: 0, 4.5: 1, 5: 2, 6.5: 3, 9: 4, 12: 4, 20: 5, 40: 5}
zfish_milestone_map = {24: 0, 48: 1, 72: 2, 120: 3, 168: 4, 216: 4, 720: 5}

h_endo = human[human["heart_layer"] == "Endocardium"].copy()
h_endo["milestone_x"] = h_endo["stage_pcw"].map(human_milestone_map)
h_endo = h_endo.groupby("milestone_x")["relative_expression_0to3"].mean().reset_index()

z_endo = zfish[zfish["heart_layer"] == "Endocardium"].copy()
z_endo["milestone_x"] = z_endo["stage_hpf"].map(zfish_milestone_map)
z_endo = z_endo.groupby("milestone_x")["relative_expression_0to3"].mean().reset_index()

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(h_endo["milestone_x"], h_endo["relative_expression_0to3"], marker="o", lw=3,
        color="#c0392b", label="Human CDH5 (endocardium)")
ax.plot(z_endo["milestone_x"], z_endo["relative_expression_0to3"], marker="s", lw=3,
        ls="--", color="#1abc9c", label="Zebrafish cdh5 (endocardium)")
ax.set_xticks(range(len(milestone_order)))
ax.set_xticklabels([m.replace(" / ", "/\n") for m in milestone_order], fontsize=8, rotation=15, ha="right")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylim(-0.4, 3.4)
ax.set_ylabel("Relative expression in endocardium")
ax.set_title("Endocardial CDH5/cdh5 (VE-cadherin) aligned across shared cardiac morphogenetic\n"
             "milestones in human and zebrafish -- both dip transiently during EndMT/cushion formation",
             fontsize=12)
ax.legend(loc="lower center")
ax.grid(alpha=0.3)
fig.text(0.5, -0.08, CAVEAT + "\nMilestone alignment per data/species_stage_correlation.csv.",
         ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(FIGS, "fig8_endocardium_cdh5_cross_species_overlay.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 9 (bonus): CDH5 vs FBN1/2/3 in human endocardium -- opposite shapes
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.5, 6))
GENE_COLORS = {"FBN1": "#7d3c98", "FBN2": "#d68910", "FBN3": "#c0392b", "CDH5": "#1f618d"}
for gene in ["FBN1", "FBN2", "FBN3"]:
    ls = human_fbn[(human_fbn["gene"] == gene) & (human_fbn["heart_layer"] == "Endocardium")].sort_values("stage_pcw")
    ax.plot(ls["stage_pcw"], ls["relative_expression_0to3"], marker="o", lw=2, alpha=0.85,
            color=GENE_COLORS[gene], label=gene)
h_cdh5 = human[human["heart_layer"] == "Endocardium"].sort_values("stage_pcw")
ax.plot(h_cdh5["stage_pcw"], h_cdh5["relative_expression_0to3"], marker="D", lw=3.5,
        color=GENE_COLORS["CDH5"], label="CDH5")
ax.axvspan(5, 6.5, color="#f1c40f", alpha=0.15)
ax.text(5.1, -0.35, "EndMT / cushion formation window", fontsize=8, color="dimgrey")
ax.set_xlabel("Post-conception week (PCW)")
ax.set_ylabel("Relative expression in endocardium")
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["undetected", "low", "moderate", "high"])
ax.set_ylim(-0.5, 3.4)
ax.set_title("CDH5 (endothelial identity) vs FBN1/2/3 (EndMT-derived ECM) in human endocardium:\n"
             "opposite roles, opposite shapes", fontsize=12)
ax.legend(loc="center right", framealpha=0.95)
ax.grid(alpha=0.3)
fig.text(0.5, -0.06, CAVEAT, ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig(os.path.join(FIGS, "fig9_endocardium_cdh5_vs_fbn_contrast.png"), dpi=160, bbox_inches="tight")
plt.close(fig)

print("Wrote figures to", FIGS)
for f in ["fig6_human_cdh5_by_layer.png", "fig7_zebrafish_cdh5_by_layer.png",
          "fig8_endocardium_cdh5_cross_species_overlay.png",
          "fig9_endocardium_cdh5_vs_fbn_contrast.png"]:
    print(" -", f)
