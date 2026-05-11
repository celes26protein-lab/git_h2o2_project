print("Rosavin SD:", np.std(rosavin))
print("L-arabinose SD:", np.std(lara))
print("Rosin SD:", np.std(rosin))

print("Rosavin SEM:", np.std(rosavin)/np.sqrt(len(rosavin)))
print("L-arabinose SEM:", np.std(lara)/np.sqrt(len(lara)))
print("Rosin SEM:", np.std(rosin)/np.sqrt(len(rosin)))

N=500
Rosavin_Avg=11.12
L_arabinose_Avg=7.69
Rosin_Avg=7.34

RosavinSD=1.66
l_araSD=1.34
rosin_Avg=1.47

| Compound    |  Mean |   SD |   SEM |
| ----------- | ----: | ---: | ----: |
| Rosavin     | 11.12 | 1.66 | 0.074 |
| L-arabinose |  7.69 | 1.34 | 0.060 |
| Rosin       |  7.34 | 1.47 | 0.066 |
