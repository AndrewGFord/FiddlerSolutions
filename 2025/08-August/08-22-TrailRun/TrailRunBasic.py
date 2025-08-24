import numpy as np

minutes_remaining = 65
exp_scores = np.zeros(minutes_remaining+1)
MINUTES_PER_MILE = 10
path_lengths = [1, 3, 3.5, 4.5]
N_PATHS = len(path_lengths)

for t in range(1, minutes_remaining+1):
    expected_score = 0
    for path_length in path_lengths:
        path_time = path_length * MINUTES_PER_MILE
        if t - path_time >= 0:
            expected_score += exp_scores[round(t - path_time)] + path_length
        else:
            expected_score += 0
    exp_scores[t] = expected_score / N_PATHS

print("Expected scores without mulligan at five-minute intervals:")
print(exp_scores[0:minutes_remaining+1:5])

print("Expected score when starting at 5:55 pm without mulligan:", exp_scores[minutes_remaining])

# Version with a mulligan- built a second array but this could have been done with a 2D array
exp_scores_mulligan = np.zeros(minutes_remaining+1)
for t in range(1, minutes_remaining+1):
    expected_score = 0
    for path_length in path_lengths:
        path_time = path_length * MINUTES_PER_MILE
        # Idea: Compare the expected score if I take the path vs if I mulligan
        score_mulligan = exp_scores[t]
        score_take_path = exp_scores_mulligan[round(t - path_time)] + path_length if t - path_time >= 0 else 0
        if score_take_path > score_mulligan:
            expected_score += exp_scores_mulligan[round(t - path_time)] + path_length
        else:
            # If the mulligan would be taken for this path length, take the score from the no-mulligan array instead
            expected_score += exp_scores[round(t)]
    exp_scores_mulligan[t] = expected_score / N_PATHS

print("Expected scores with mulligan at five-minute intervals:")
print(exp_scores_mulligan[0:minutes_remaining+1:5])

print("Expected score when starting at 5:55 pm with mulligan:", exp_scores_mulligan[minutes_remaining])