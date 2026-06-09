# Effect of Rosavin, Rosin, and L-(+)-Arabinose on H2O2

Molecular dynamics (MD) simulation project using GROMACS.
paper: https://www.biorxiv.org/content/10.64898/2026.05.21.726678v1
"Antioxidant properties of Rhodiola rosea" (May 2026 Drew et al.,)
---

## Overview

This project investigates the interactions between hydrogen peroxide (H₂O₂) and three compounds:

- Rosavin
- Rosin
- L-(+)-Arabinose

The experiments revealed that rosavin exhibited a significant protective effect against H₂O₂-induced oxidative stress.

To support these experimental observations, molecular dynamics (MD) simulations were performed using GROMACS to analyze:

- Minimum distance between compounds and H₂O₂
- Radial distribution functions (RDFs)
- Hydrogen-bond networks

---

## Objectives

The goal of this study was to compare molecular interactions between H₂O₂ and each compound and identify possible mechanisms underlying the antioxidant effect of rosavin.

---

# Methods

## Software

- GROMACS
- PyMOL
- Python
- NumPy
- Matplotlib

---

## MD Analyses

### 1. Minimum Distance Analysis- center-of-mass calculation  (COM)

The center-of-mass (COM) distance describes the overall separation between two molecules by measuring the distance between their average mass positions rather than the distance between individual atoms. In MD simulations, this provides information about how far apart the molecules are overall during the trajectory. However, even when the COM distance is relatively large, specific atoms or flexible regions of the molecules may still transiently approach each other closely and form local interactions such as hydrogen bonds. Therefore, COM distance reflects global molecular separation, whereas minimum atom-to-atom distance reflects local molecular contact.

### 2. Radial Distribution Function (RDF)

RDF analysis was performed to evaluate local molecular distributions around H₂O₂.

### 3. Hydrogen Bond Analysis

Hydrogen-bond formation and stability were analyzed to investigate intermolecular interactions.

---

# Results

## Key Findings

- Rosavin showed stronger and more stable interactions with H₂O₂ compared to rosin and L-(+)-arabinose.

- RDF analysis suggested enhanced local accumulation of H₂O₂ around rosavin.

- Hydrogen-bond analysis indicated more persistent intermolecular hydrogen bonding in the rosavin system.

These findings support the experimentally observed protective effect of rosavin against oxidative stress.O

