import matplotlib.pyplot as plt
import numpy as np

# ===== compounds =====
compounds = ["Rosavin", "L-arabinose", "Rosin"]

# ===== average H-bonds =====
hbonds = [11.12, 7.69, 7.34]

# ===== create figure =====
plt.figure(figsize=(6,5))

# ===== bar plot =====
bars = plt.bar(compounds, hbonds)

# ===== labels =====
plt.ylabel("Average H-bonds")
plt.xlabel("Compounds")
plt.title("Solute-Water Hydrogen Bond Network")

# ===== add values on bars =====
for i, value in enumerate(hbonds):
    plt.text(i, value + 0.15, f"{value:.2f}", ha='center')

# ===== significance line =====
y = 12.2

plt.plot([0, 0, 2, 2], [y, y+0.2, y+0.2, y], lw=1.5)

# ===== significance stars =====
plt.text(1, y+0.25, "***", ha='center', fontsize=16)

# ===== ANOVA result text =====
plt.text(
    0.02,
    0.95,
    "ANOVA: F = 974.7\np < 0.001",
    transform=plt.gca().transAxes,
    verticalalignment='top'
)

# ===== y-axis limit =====
plt.ylim(0, 13.5)

# ===== layout =====
plt.tight_layout()

# ===== save =====
plt.savefig("hbond_overall_stats.png", dpi=300)

# ===== show =====
plt.show()