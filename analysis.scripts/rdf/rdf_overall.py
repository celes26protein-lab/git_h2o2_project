import numpy as np
import matplotlib.pyplot as plt

# ===== load xvg files =====
rosavin = np.loadtxt("rdf_rosavin.xvg", comments=["@", "#"])
rosin = np.loadtxt("rdf_rosin.xvg", comments=["@", "#"])
lara = np.loadtxt("rdf_l-ara.xvg", comments=["@", "#"])

# ===== extract columns =====
r_rosavin = rosavin[:, 0]
g_rosavin = rosavin[:, 1]

r_rosin = rosin[:, 0]
g_rosin = rosin[:, 1]

r_lara = lara[:, 0]
g_lara = lara[:, 1]

# ===== plot =====
plt.figure(figsize=(6,5))

plt.plot(r_rosavin, g_rosavin, label="Rosavin")
plt.plot(r_rosin, g_rosin, label="Rosin")
plt.plot(r_lara, g_lara, label="L-(+)-Arabinose")

# ===== labels =====
plt.xlabel("Distance (nm)")
plt.ylabel("g(r)")
plt.title("RDF between H2O2 and Compounds")

# ===== legend =====
plt.legend()

# ===== save =====
plt.savefig("rdf_overall.png", dpi=300)

# ===== show =====
plt.show()