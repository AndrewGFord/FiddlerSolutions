import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# rewrite to include number of cards in deck as a parameter?
minDS = 2
maxDS = 100
deckSize = 52
nTrials = 10000
#isEC = False
results = pd.DataFrame(columns=['Cards_In_Deck','Win_Pct_Original','Win_Pct_EC'])
results.loc[0] = [1,0.0,0.0] # the case with 1 card in each deck is trivial

# tells whether two values are equal mod 52
# written to work with both the original problem statement and the extra credit
def cardsEqual(c1,c2,ds=deckSize):
	return (c1%ds)==(c2%ds)

def shuffleCards(nmin,nmax):
	cards = np.zeros(nmax-nmin+1)
	for ii in range(nmin,nmax+1):
		cards[ii-nmin] = ii
	random.shuffle(cards)
	return cards

def setupDecks(isEC,ds=deckSize):
	if isEC:
		allCards = shuffleCards(1,ds*2)
		deck1 = allCards[0:ds]
		deck2 = allCards[ds:(2*ds)]
	else:
		deck1 = shuffleCards(1,ds)
		deck2 = shuffleCards(ds+1,2*ds)
	decks = np.column_stack((deck1, deck2))
	return decks

def singleTrial(isEC,ds=deckSize):
	decks = setupDecks(isEC,ds)
	gameLost = False
	ii = 0
	while((gameLost == False) & (ii < ds)):
		cardMatch = cardsEqual(decks[ii,0],decks[ii,1],ds)
		if cardMatch:
			gameLost = True
		else:
			ii += 1
	return (gameLost == False)

for ds in range(minDS,maxDS+1):
	winsOrig = 0
	winsEC = 0
	for ii in range(nTrials):
		gameWon = singleTrial(False,ds)
		if gameWon:
			winsOrig += 1
		gameWon = singleTrial(True,ds)
		if gameWon:
			winsEC += 1
	#print(wins/nTrials)
	results.loc[len(results['Cards_In_Deck'])] = [ds,winsOrig/nTrials,winsEC/nTrials]
	if ds == 52:
		print("Original problem solution:",winsOrig/nTrials)
		print("Extra credit solution:",winsEC/nTrials)

plt.scatter(x=results['Cards_In_Deck'],y=results['Win_Pct_Original'],label='Original game')
plt.scatter(x=results['Cards_In_Deck'],y=results['Win_Pct_EC'],label='Extra credit variation')
plt.legend(loc="upper right")
plt.ylim(0.0,1.0)
plt.xlabel("Number of cards in each deck")
plt.ylabel("Winning percentage")
plt.title("Approximate winning percentage by deck size")
plt.show()

print(results.head(5))
	