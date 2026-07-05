"""Generate a 5x5 likelihood/impact risk heat map from risk_register.csv."""

import csv
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INPUT_FILE = "risk_register.csv"
OUTPUT_PNG = "risk_heatmap.png"


def zone_color(score):
    if score <= 4:
        return "#63BE7B"   # Low - green
    if score <= 9:
        return "#FFEB84"   # Medium - yellow
    if score <= 14:
        return "#FFA64D"   # High - orange
    return "#F8696B"       # Critical - red


def main():
    cells = defaultdict(list)
    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cells[(int(row["Impact"]), int(row["Likelihood"]))].append(row["Risk_ID"])

    fig, ax = plt.subplots(figsize=(10, 8))
    for impact in range(1, 6):
        for likelihood in range(1, 6):
            score = impact * likelihood
            ax.add_patch(Rectangle((impact - 0.5, likelihood - 0.5), 1, 1,
                                   facecolor=zone_color(score),
                                   edgecolor="white", linewidth=2))
            ax.text(impact - 0.44, likelihood + 0.38, str(score),
                    fontsize=8, color="#555", va="top")
            ids = cells.get((impact, likelihood))
            if ids:
                ax.text(impact, likelihood, "\n".join(ids),
                        ha="center", va="center", fontsize=9,
                        fontweight="bold", color="#1a1a1a")

    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impact", fontsize=12, fontweight="bold")
    ax.set_ylabel("Likelihood", fontsize=12, fontweight="bold")
    ax.set_title("Enterprise Risk Heat Map — 5x5 Likelihood x Impact",
                 fontsize=14, fontweight="bold", pad=15)
    ax.set_aspect("equal")

    legend = [Rectangle((0, 0), 1, 1, facecolor=c) for c in
              ("#63BE7B", "#FFEB84", "#FFA64D", "#F8696B")]
    ax.legend(legend, ["Low (1-4)", "Medium (5-9)", "High (10-14)",
                       "Critical (15-25)"],
              loc="upper left", bbox_to_anchor=(1.02, 1), title="Risk Zone")

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150)
    print(f"Heat map saved to {OUTPUT_PNG}")


if __name__ == "__main__":
    main()
