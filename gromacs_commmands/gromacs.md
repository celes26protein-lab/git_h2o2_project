# GROMACS MD Simulation

## System Preparation

The simulation system was prepared using GROMACS.

### 1. Simulation box generation

```bash
gmx editconf -f rosavin.gro -o boxed.gro -c -d 1.0 -bt cubic
```

### 2. Solvation with SPC/E water model

```bash
gmx solvate -cp boxed.gro -cs spc216.gro -o solvated.gro -p system.top
```

### 3. H₂O₂ insertion

```bash
gmx insert-molecules -f solvated.gro -ci h2o2.gro -nmol N_H2O2 -o system_final.gro
```

---

## Force Field and Models

| Compound | Model |
|---|---|
| Rosavin | GAFF (ACPYPE) |
| Rosin | GAFF (ACPYPE) |
| L-arabinose | GAFF / ACPYPE |
| H₂O₂ | Fixed small molecule |
| Water | SPC/E |
