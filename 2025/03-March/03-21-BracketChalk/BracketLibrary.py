# Library functions for computing bracket probabilities
#import numpy as np

def win_probability_one_matchup(seed,opp_seed):
	return opp_seed/(seed+opp_seed)

# combine opp_seeds and opp_probs into a 2-column or 2-row array?
def advance_probability(seed,opp_seeds,opp_probs):
	output = 0
	num_opps = len(opp_seeds)
	for ii in range(num_opps):
		output += win_probability_one_matchup(seed,opp_seeds[ii])*opp_probs[ii]
	return output

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
	probs = []
	for ii in range(n_teams):
		probs.append(1)
	return teams,probs

def get_possible_opponent_indices(idx,n_opponents):
	# group ranges from 0 to n-1
	# where n is the number of teams playing in the round
	group = idx//n_opponents
	if group%2 == 0:
		opp_group = group + 1
	else:
		opp_group = group - 1
	opp_start_idx = opp_group * n_opponents
	opp_end_idx = opp_start_idx + n_opponents
	return opp_start_idx,opp_end_idx

# output probabilities can only be trusted if called in proper context
def get_possible_opponents(idx,round_number,teams,probs):
	n_opponents = 2**round_number # round_number indexes from 0
	start_idx, end_idx = get_possible_opponent_indices(idx,n_opponents)
	output_teams = teams[start_idx:end_idx]
	output_probs = probs[start_idx:end_idx]
	return output_teams,output_probs

# round_number: The round being played. Indexes from 0
# teams: List of teams
# probs: List of teams, with the probability of each team reaching this round
def advance_all_probabilities(round_number,teams,probs):
	n_teams = len(teams)
	probs_new = []
	n_opponents = 2**round_number # round_number indexes from 0
	for ii in range(n_teams):
		opp_seeds,opp_probs = get_possible_opponents(ii,round_number,teams,probs)
		new_prob = advance_probability(teams[ii],opp_seeds,opp_probs)
		probs_new.append(new_prob*probs[ii])
	return probs_new