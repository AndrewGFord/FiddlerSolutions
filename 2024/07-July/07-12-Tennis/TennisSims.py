import numpy as np
import random

def playPoint():
	return random.randint(1,2)

# target: number of points needed to win
#	target = 4 for regular game, 7 for tiebreak
def playGame(target):
	#p1Score = 0
	#p2Score = 0
	scores = [0,0]
	done = False
	while done == False:
		pt = playPoint()
		scores[pt-1] += 1
		if max(scores) >= target and abs(scores[0]-scores[1]) >= 2:
			done = True
	return scores

def playSet():
	totPoints = [0,0]
	gameWins = [0,0]
	gamesPlayed = 0
	gmTarget = 4
	tbTarget = 7
	playAnotherGame = True
	while playAnotherGame == True:
		[p1Score,p2Score] = playGame(gmTarget)
		gamesPlayed += 1
		totPoints[0] += p1Score
		totPoints[1] += p2Score
		if p1Score > p2Score:
			gameWins[0] += 1
		else:
			gameWins[1] += 1
		if gamesPlayed == 12:
			break;
		elif max(gameWins) == 6 and min(gameWins) <= 4:
			break;
	if gameWins[0] == gameWins[1]:
		[p1Score,p2Score] = playGame(tbTarget)
		totPoints[0] += p1Score
		totPoints[1] += p2Score
		if p1Score > p2Score:
			gameWins[0] += 1
		else:
			gameWins[1] += 1
	if gameWins[0] > gameWins[1]:
		winner = 1
	else:
		winner = 2
	return [winner,totPoints[0],totPoints[1]]

# return match winner and total points scored by each player
# giving totals for both accounts properly for ties
def playMatch():
	totPoints = [0,0]
	setsWon = [0,0]
	while max(setsWon) < 2:
		[winner,pts1,pts2] = playSet()
		totPoints = np.add(totPoints,np.array([pts1,pts2]))
		setsWon[winner-1] += 1
	if setsWon[0] == 2:
		matchWinner = 1
	else:
		matchWinner = 2
	return [matchWinner,totPoints[0],totPoints[1]]

nMatches = 1000000
nMatchWinPtsLoss = 0
nTies = 0
for ii in range(nMatches):
	[matchWinner,pts1,pts2] = playMatch()
	if matchWinner == 1 and pts2 > pts1:
		nMatchWinPtsLoss += 1
	elif matchWinner == 2 and pts1 > pts2:
		nMatchWinPtsLoss += 1
	elif pts1 == pts2:
		nTies += 1
		
# output data
print("Total matches: ", nMatches)
print("----------")
print("Total matches where the winner won fewer points: ", nMatchWinPtsLoss)
print("Percentage: ",100.0*nMatchWinPtsLoss/nMatches)
print("----------")
print("Total matches where both players won the same number of points: ",nTies)
print("Percentage: ",100.0*nTies/nMatches)
