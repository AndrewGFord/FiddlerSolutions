import random

N_TRIALS = 192000
wins = 0

def check_win_sprint(you, opp_1, opp_2):
	if opp_1 < 0.5:
		opp_1 = 0
	if opp_2 < 0.5:
		opp_2 = 0
	return (you > opp_1 and you > opp_2)

def check_can_win_coast(opp_1, opp_2):
	return (opp_1 < 0.5 and opp_2 < 0.5)

for i in range(N_TRIALS):
	energy_cutoff = random.random()
	your_energy = random.random()
	opponent_energy_1 = random.random()
	opponent_energy_2 = random.random()
	if your_energy > energy_cutoff:
		if check_win_sprint(your_energy, opponent_energy_1, opponent_energy_2):
			wins += 1
	else:
		if check_can_win_coast(opponent_energy_1, opponent_energy_2):
			toss_up_value = random.random()
			if toss_up_value < 1.0/3.0:
				wins += 1

print(f"Expected wins by theory with {N_TRIALS} trials: 59000")
print(f"Simulated wins in {N_TRIALS} trials: {wins}")