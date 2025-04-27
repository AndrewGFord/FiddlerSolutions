import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def check_tree_seen(x,y):
	return math.gcd(x,y) == 1

def check_distance(x,y,d):
	return (x * x) + (y * y) <= (d * d)

def get_angle_degrees(x,y):
	return math.atan(y/x)*180/math.pi

max_max_distance = 100

column_names = ['Max Vision Dist','Angle 1st','Window 1st','Angle 5th','Window 5th']
angles_df = pd.DataFrame(columns=column_names)

for max_distance in range(6,max_max_distance):
	tree_angles = []
	list_len = 0
	
	for x in range(1,max_distance+1):
		for y in range(x+1):
			if (check_distance(x,y,max_distance) & check_tree_seen(x,y)):
				angle = get_angle_degrees(x,y)
				i = 0
				tree_angles.append(angle)
				list_len += 1
	
	tree_angles.sort()
	angle_windows = []
	for i in range(list_len-1):
		window = tree_angles[i+1]-tree_angles[i]
		angle_windows.append(window)
	angle_windows_sums = []
	
	# angle_windows has a length 1 less than tree_angles
	# list_len - 2 used to save a tiny bit of memory
	for i in range(list_len-2):
		angle_windows_sums.append(angle_windows[i] + angle_windows[i+1])
		
	# needs +2 instead of +1 because value of np.argmax is relative to the shortened list input into it
	max_angle_idx = np.argmax(angle_windows_sums[1:-1]) + 2
	#print(tree_angles[max_angle_idx])
	
	# get full rankings by making a pandas dataframe and sorting it
	angle_windows_sums_cut = angle_windows_sums[1:-1]
	num_rows = len(angle_windows_sums_cut)
	angles = [tree_angles[i+2] for i in range(num_rows)]
	
	df = pd.DataFrame(list(zip(angles,angle_windows_sums_cut)),
		columns = ['Angle', 'Full Width'])
	df = df.sort_values(by=['Full Width'], ascending=False)
	df = df.reset_index(drop=False)
	
	widest_angle_1 = df.at[0, 'Angle']
	widest_window_1 = df.at[0, 'Full Width']
	widest_angle_5 = df.at[4, 'Angle']
	widest_window_5 = df.at[4, 'Full Width']
	
	new_row = {
		'Max Vision Dist': max_distance,
		'Angle 1st': widest_angle_1,
		'Window 1st': widest_window_1,
		'Angle 5th': widest_angle_5,
		'Window 5th': widest_window_5
	}
	angles_df.loc[len(angles_df)] = new_row

print(angles_df)

# Makes a plot of the angle with the widest window and the angle with the 5th widest window
scatter_angle_1 = plt.scatter(x=angles_df['Max Vision Dist'],y=angles_df['Angle 1st'],
	label='Angle with widest window')
scatter_angle_5 = plt.scatter(x=angles_df['Max Vision Dist'],y=angles_df['Angle 5th'],
	label='Angle with fifth widest window')
plt.title('Angle surrounded by the widest gaps')
plt.xlabel('Farthest distance seen')
plt.ylabel('Angle (degrees)')
plt.legend(handles=[scatter_angle_1, scatter_angle_5])
plt.show()

# Makes a plot of the corresponding window widths
scatter_window_1 = plt.scatter(x=angles_df['Max Vision Dist'],y=angles_df['Window 1st'],
	label='Widest window')
scatter_window_5 = plt.scatter(x=angles_df['Max Vision Dist'],y=angles_df['Window 5th'],
	label='Fifth widest window')
plt.title('Widest and fifth widest gaps')
plt.xlabel('Farthest distance seen')
plt.ylabel('Width of window (degrees)')
plt.legend(handles=[scatter_window_1, scatter_window_5])
plt.show()