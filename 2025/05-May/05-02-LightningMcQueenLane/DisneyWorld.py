import numpy as np

# Average number of rides after the third
# index is how many open time slots are left after the third
# can range from 0 to 9
avg_rides_left = np.zeros(10)
for i in range(1,10):
	avg_rides_left[i] = 1 + np.mean(avg_rides_left[:i])

#print(avg_rides_left)

# average it out based on all original 3-time-slot combos
total_initial_combos = 12*11*10//6
total_exp_rides = 0

for i in range(10):
	for j in range(i+1,11):
		for k in range(j+1,12):
			total_exp_rides += avg_rides_left[11-k] # more efficient to add 3 later

exp_num_rides = total_exp_rides/total_initial_combos + 3
print(f'On average, you can expect to use the Lightning Lane for {exp_num_rides} rides.')