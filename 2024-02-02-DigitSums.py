## For how many whole numbers N between 1 and 10,000 inclusive does f(N) = 3?
## Extra credit February 2, 2024

import numpy as np

maxNum = 10000
nums = range(maxNum+1) # includes 0 to avoid offsetting indices by 1 in code
fNums = np.zeros(maxNum+1) # includes 0 to avoid offsetting indices by 1 in code

def digitSum(n):
	total = 0
	while n > 0:
		lastDigit = n%10
		total += lastDigit
		n = n//10
	return total

for n in range(10,maxNum+1):
	ds = digitSum(n)
	fNums[n] = fNums[ds]+1

print(np.count_nonzero(fNums == 3))