import numpy as np

n_chars = 10
combinations = np.zeros(n_chars + 1)
if n_chars > 0:
	combinations[1] = 1
if n_chars > 1:
	combinations[2] = 2
if n_chars > 2:
	combinations[3] = 4
for i in range(4,n_chars+1):
	combinations[i] = combinations[i-1] + combinations[i-2] + combinations[i-3]
print(combinations)
print(f"Number of combinations for {n_chars} I's: {combinations[n_chars]}")