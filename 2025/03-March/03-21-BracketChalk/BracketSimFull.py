import BracketLibrary as bl
import numpy as np
import matplotlib.pyplot as plt

ROUNDS_MAX = 12
results = np.zeros([2,ROUNDS_MAX])
HIGHLIGHT_ORIGINAL_PROBLEM = True
SAVE_PLOT = True

for rounds in range(1,ROUNDS_MAX+1):
	teams,probs = bl.build_team_list(rounds)
	for ii in range(rounds):
		probs = bl.advance_all_probabilities(ii,teams,probs)
	results[0,rounds-1] = rounds
	results[1,rounds-1] = probs[0]
	if rounds == 4:
		print(f'Probability that the 1-seed wins in a 16-team bracket: {probs[0]}')

#print(results)
fig, ax = plt.subplots(figsize=(12,6))
bar_colors = []
for ii in range(1,ROUNDS_MAX+1):
	if HIGHLIGHT_ORIGINAL_PROBLEM and (ii == 4):
		bar_colors.append('tab:orange')
	else:
		bar_colors.append('tab:blue')
bars = ax.bar(results[0],results[1],color=bar_colors)
results_display = ["%0.4f" % ii for ii in results[1]]
ax.bar_label(bars,results_display)
ax.set_title('Probability of the 1-seed winning its region')
ax.set_xlabel('Number of rounds within regional play')
plt.show()
if SAVE_PLOT:
	plt.savefig('BracketSimBarGraph.png')