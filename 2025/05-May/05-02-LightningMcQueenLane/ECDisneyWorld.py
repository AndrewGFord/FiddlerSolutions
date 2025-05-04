import numpy as np

# more general than needed (j always less than k)
def order_triplet(triplet):
	min_index = np.argmin(triplet)
	max_index = np.argmax(triplet)
	mid_index = 3-min_index-max_index
	return [triplet[min_index],triplet[mid_index],triplet[max_index]]

exp_values = np.zeros((10,11,12))
exp_values[9,10,11] = 3.0
total_exp_values = 3.0
total_initial_combinations = 12*11*10/6
# situation represented: just finished the "first" ride on the pass, getting a replacement
# i: first ride on pass
# j: second ride on pass
# k: third ride on pass
# l: iterates through possible replacements for i
for i in range(8,-1,-1):
	for j in range(i+1,11):
		for k in range(j+1,12):
			total = 0
			possibilities = 9-i
			for l in range(i+1,12):
				if l == j or l == k:
					pass
				else:
					[a,b,c] = order_triplet([j,k,l])
					total += exp_values[a,b,c]
			term_to_add = 1 + (total / possibilities)
			exp_values[i,j,k] = term_to_add
			total_exp_values += term_to_add
avg_num_rides = total_exp_values/total_initial_combinations
print(f'On average, you can expect to use the Lightning Lane for {avg_num_rides} rides.')