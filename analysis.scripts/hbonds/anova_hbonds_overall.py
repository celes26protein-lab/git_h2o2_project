import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# =========================
# Load H-bond data
# =========================
# hbnum.xvg format:
# time   hbonds
#
# Skip lines starting with # or @

def load_hbond_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#') or line.startswith('@'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                data.append(float(parts[1]))
    return np.array(data)

# =========================
# Load each trajectory
# =========================

rosavin = load_hbond_data("hbnum_rosavin.xvg")
larabinose = load_hbond_data("hbnum_l-ara.xvg")
rosin   = load_hbond_data("hbnum_rosin.xvg")

# =========================
# Calculate statistics
# =========================

means = [
    np.mean(rosavin),
    np.mean(larabinose),
    np.mean(rosin)
]

stds = [
    np.std(rosavin),
    np.std(larabinose),
    np.std(rosin)
]

labels = ["Rosavin", "L-arabinose", "Rosin"]

# =========================
# ANOVA
# =========================

F, p = stats.f_oneway(rosavin, larabinose, rosin)

# =========================
# Plot
# =========================

fig, ax = plt.subplots(figsize=(8,6))

bars = ax.bar(
    labels,
    means,
    yerr=stds,
    capsize=6
)

# Add values on bars
for bar, mean, std in zip(bars, means, stds):
    ax.text(
        bar.get_x() + bar.get_width()/2,
        mean + std + 0.2,
        f"{mean:.2f} ± {std:.2f}",
        ha='center',
        fontsize=11
    )

# Labels
ax.set_ylabel("Average H-bonds")
ax.set_xlabel("Compounds")
ax.set_title("Average Solute–Water Hydrogen Bonds")

# ANOVA text
ax.text(
    1.02,
    0.95,
    f"ANOVA: F = {F:.2f}\np = {p:.3e}",
    transform=ax.transAxes,
    fontsize=11,
    verticalalignment='top'
)

plt.tight_layout()
plt.show()

