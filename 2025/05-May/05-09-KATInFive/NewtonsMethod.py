import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return ((20*x-60)*x+61)*x-20

def df(x):
	return (60*x-120)*x+61

x_vals = np.linspace(0.6,0.75,1001)
y_vals = f(x_vals)
plt.plot(x_vals,y_vals)
plt.show()

eps = 1e-8
x = 0.65
diff = 1

while abs(diff)>eps:
	diff = f(x)/df(x)
	x_new = x-diff
	x = x_new

print(f'The two probabilities are equal at approximately p={x}.')

print(f'Given that the most likely outcome is a win in 5 games, the probability that winning in 4 is more likely than a 7-game series is {(0.75-x)/0.15}.')