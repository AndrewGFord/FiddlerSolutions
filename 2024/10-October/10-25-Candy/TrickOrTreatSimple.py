#import numpy as np

pbSum = 1/6
epsilon = 0.000000001
n = 1
diff = 1 # placeholder
# diff must be greater than epsilon to not immediately leave while loop
limitSum = 0 #placeholder


while diff > epsilon:
	pbSum += 1/((n+1)*(n+2)*(n+3))
	n += 1
	lsPrev = limitSum
	limitSum = 0
	for j in range(n):
		limitSum += j/((j+1)*(j+2)*(j+3))/pbSum
	diff = limitSum - lsPrev
	#print(n,"  ",pbSum,"  ",limitSum,"  ",diff)

print("n: ",n)
print("pbSum: ",pbSum)
print("limitSum: ",limitSum)
print("diff: ",diff)
	