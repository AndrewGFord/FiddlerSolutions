# Simulate a bracket of 64 teams, seeded 1-64
# Each team has a power rating of 65-seed
# Each underdog gets a constant boost B to its power rating
# B is positive and not an integer
# Team with higher power rating including underdog boost wins each time

import numpy as np
import pandas as pd

IMPORT_ACTUAL_BRACKET = False
BRACKET_FILENAME = 'MensBracket2025.csv' # plug in file name of imported bracket
if IMPORT_ACTUAL_BRACKET:
	N_ROUNDS = 7
	FAKE_TEAMS = 60
	OUTPUT_FILENAME = 'MensBracketSimChamps2025.csv'
else:
	N_ROUNDS = 6
	FAKE_TEAMS = 0
	OUTPUT_FILENAME = 'BracketSim.csv'
N_TEAMS = 2**N_ROUNDS
wins = np.zeros(N_TEAMS-FAKE_TEAMS)

def get_power_rating(seed, n_teams):
	return n_teams + 1 - seed

# Given the seeds of two teams in a game
# and the value of B
# returns the seed of the winner of the game
def decide_game(seed_1, seed_2, team_1, team_2, boost, n_teams):
	rating_1 = get_power_rating(seed_1, n_teams)
	rating_2 = get_power_rating(seed_2, n_teams)
	if rating_1 < rating_2:
		rating_1 += boost
	else:
		rating_2 += boost
		
	if rating_1 < rating_2:
		winner = seed_2
		win_team = team_2
	else:
		winner = seed_1
		win_team = team_1
	
	return winner,win_team

# Generate starting bracket - can copy from previous week's code
# modified to remove probabilities- those aren't needed anymore
def build_team_list(n_rounds):
	n_teams = 2**n_rounds
	teams = [1]
	team_count = 1
	for ii in range(n_rounds):
		teams_new = []
		round_sum = 2*team_count+1
		for jj in range(team_count):
			teams_new.append(teams[jj])
			teams_new.append(round_sum - teams[jj])
		teams = teams_new
		team_count *= 2
	return teams

# Function to compute the winner of a bracket
def play_tournament(boost,bracket_data):
	if (IMPORT_ACTUAL_BRACKET):
		seed_list = bracket_data['Seed']
		team_list = bracket_data['Team']
	else:
		seed_list = build_team_list(N_ROUNDS)
		team_list = build_team_list(N_ROUNDS)
	for ii in range(N_ROUNDS):
		seed_list,team_list = play_round(seed_list,team_list,boost)
	champion = seed_list[0]
	return champion

# Function to compute all winners of a given round
def play_round(seed_list,team_list,boost):
	n_teams = len(seed_list)
	n_games = n_teams//2
	new_seed_list = []
	new_team_list = []
	for jj in range(n_games):
		seed_1 = seed_list[2*jj]
		team_1 = team_list[2*jj]
		seed_2 = seed_list[2*jj+1]
		team_2 = team_list[2*jj+1]
		seed_advance,team_advance = decide_game(seed_1,seed_2,team_1,team_2,boost,n_teams)
		new_seed_list.append(seed_advance)
		new_team_list.append(team_advance)
	return new_seed_list,new_team_list

if IMPORT_ACTUAL_BRACKET:
	bracket_data = pd.read_csv(BRACKET_FILENAME)
else:
	bracket_data = ''
# Only need to check B = 0.5, 1.5, 2.5, ..., 63.5
for ii in range(N_TEAMS-FAKE_TEAMS):
	b = ii + 0.5
	champion = play_tournament(b,bracket_data)
	wins[champion-1] += 1

never_won = np.count_nonzero(wins==0)
if IMPORT_ACTUAL_BRACKET:
	bracket_data_clean = bracket_data[bracket_data['Seed']<999].sort_values(by='Seed')
	bracket_data_clean.insert(2,'Wins',wins)
	print(bracket_data_clean.head(5))
	bracket_data_clean.to_csv(OUTPUT_FILENAME,index=True)
print(f'Number of teams that cannot win for any value of B: {never_won}')