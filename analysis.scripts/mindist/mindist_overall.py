import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

rosavin = np.loadtxt(
    "mindist_rosavin.xvg",
    comments=["#", "@"]
)

rosin = np.loadtxt(
    "mindist_rosin.xvg",
    comments=["#", "@"]
)

l_arabinose = np.loadtxt(
    "mindist_l.xvg",
    comments=["#", "@"]
)

# Extract distance values
rosavin_dist = rosavin[:, 1]
rosin_dist = rosin[:, 1]
l_dist = l_arabinose[:, 1]

# ANOVA
F_value, p_value = f_oneway(
    rosavin_dist,
    rosin_dist,
    l_dist
)

print("F-value:", F_value)
print("p-value:", p_value)

# Mean values
means = [
    np.mean(rosavin_dist),
    np.mean(rosin_dist),
    np.mean(l_dist)
]

labels = [
    "Rosavin",
    "Rosin",
    "L-arabinose"
]

# Bar graph
plt.figure(figsize=(6,5))
plt.bar(labels, means)

plt.ylabel("Average Minimum Distance (nm)")
plt.title("Comparison of Minimum Distances")

# Display ANOVA result on graph
plt.text(
    0,
    max(means)*0.95,
    f"F = {F_value:.3f}\np = {p_value:.3e}",
    fontsize=10
)

plt.tight_layout()

# Save figure
plt.savefig("mindist_bargraph.png", dpi=300)

plt.show()