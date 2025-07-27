import numpy as np
import matplotlib.pyplot as plt

c_vals = np.linspace(0,1,1001)

def foo(c):
	if c > 0.5:
		return c/12 + (1-c*c*c)/3
	else:
		return 5/12 - c/6

y_vals = np.zeros(1001)
for i in range(1001):
	y_vals[i] = foo(c_vals[i])

plt.plot(c_vals,y_vals)
plt.xlabel("Cutoff energy level (as percent)")
plt.ylabel("Probablity of winning (as decimal)")
plt.title("Probability of winning based on the cutoff value you guess")
plt.show()