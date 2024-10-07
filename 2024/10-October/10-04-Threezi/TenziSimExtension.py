import numpy as np
import random
from scipy import stats
import matplotlib.pyplot as plt

def rollDie(nFaces):
	return random.randint(1,nFaces)

def rollDice(nDice,nFaces):
	rolls = np.zeros(nDice)
	rollCounts = np.zeros(nFaces)
	for i in range(nDice):
		result = rollDie(nFaces)
		rolls[i] = result
	return rolls

maxNumDice = 25
numFacesOptions = [4,6,8,12,20]
numFaceChoices = len(numFacesOptions)
nTrials = 10000
modeAvgs = np.zeros([numFaceChoices,maxNumDice])
for i in range(numFaceChoices):
	nFaces = numFacesOptions[i]
	for nd in range(1,maxNumDice+1):
		if (nd == 1):
			mAvg = 1
		else:
			modes = np.zeros(nd)
			for j in range(nTrials):
				rolls = rollDice(nd,nFaces)
				m = stats.mode(rolls,keepdims=False)
				nSaved = m[1]
				modes[nSaved-1] += 1
			numer = 0
			for k in range(nd):
				numer += (k+1)*modes[k]
			mAvg = numer/nTrials
		modeAvgs[i,nd-1] = mAvg

plt.scatter(x=range(1,maxNumDice+1),y=modeAvgs[0,:],label='4-sided dice')
plt.scatter(x=range(1,maxNumDice+1),y=modeAvgs[1,:],label='6-sided dice')
plt.scatter(x=range(1,maxNumDice+1),y=modeAvgs[2,:],label='8-sided dice')
plt.scatter(x=range(1,maxNumDice+1),y=modeAvgs[3,:],label='12-sided dice')
plt.scatter(x=range(1,maxNumDice+1),y=modeAvgs[4,:],label='20-sided dice')
plt.legend(loc="upper left")
plt.xlabel('Number of dice')
plt.ylabel('Average number of dice saved')
plt.title('Extending Tenzi to other numbers and sizes of dice')
plt.show()