import matplotlib.pyplot as plt
import numpy as np

p_vals = np.linspace(0.5,1.0,10001)

p_win_4 = p_vals**4
p_win_5 = (p_win_4)*(1-p_vals)*4
p_win_6 = (p_win_5)*(1-p_vals)*10/4
p_win_7 = (p_win_6)*(1-p_vals)*2

plt.plot(p_vals,p_win_4)
plt.plot(p_vals,p_win_5)
plt.plot(p_vals,p_win_6)
plt.plot(p_vals,p_win_7)
plt.xlabel('Probability of winning each game')
plt.title('Probability of winning the series in a specific number of games')
plt.legend(['Win in 4', 'Win in 5', 'Win in 6', 'Win in 7'])
plt.savefig('SeriesWinProbabilities.png')
plt.show()
