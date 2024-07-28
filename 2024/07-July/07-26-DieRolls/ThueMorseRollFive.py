import numpy as np

a = 1.0/6.0
b = 5.0/36.0
pcoeff = 5.0/6.0
eps = 1e-16

for i in range (3,101):
	pcoeff = pcoeff*pcoeff
	aTerm = pcoeff*b
	bTerm = pcoeff*a
	a += aTerm
	b += bTerm
	if 1-a-b < eps:
		print("Exited loop after i = ", i)
		break

print("Probability A wins: ", a)
print("Probability B wins: ", b)
print("Ratio: ", a/(a+b))