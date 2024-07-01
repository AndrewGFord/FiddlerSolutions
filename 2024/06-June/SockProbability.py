import numpy as np

def probFirstMatch(n):
	denom = 10*9*8*7*6
	numer = (2**(n-1))*(n-1)*(10-n)*(9-n)*(8-n)*(7-n)
	return numer/denom

runningTotal = 0

for ii in range(2,7):
	prob = probFirstMatch(ii)
	runningTotal += prob
	print(ii, prob)

print("")
print(runningTotal)