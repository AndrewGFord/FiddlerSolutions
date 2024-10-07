import numpy as np
import random
from scipy import stats

def rollDie(nFaces):
	return random.randint(1,nFaces)

def rollDice(nDice,nFaces):
	rolls = np.zeros(nDice)
	rollCounts = np.zeros(nFaces)
	for i in range(nDice):
		result = rollDie(nFaces)
		rolls[i] = result
		#rollCounts[result-1] += 1
	return rolls

nTrials = 10000000
numberDice = 10
numberFaces = 6
modes = np.zeros(numberDice)

for j in range(nTrials):
	rolls = rollDice(numberDice,numberFaces)
	#print(rolls)
	m = stats.mode(rolls)
	nSaved = m[1]
	modes[nSaved-1] += 1
	#print('Trial complete! Number of dice saved: ', nSaved)

print(modes)
numer = 0
for j in range(numberDice):
	numer += (j+1)*modes[j]

print(numer/nTrials)