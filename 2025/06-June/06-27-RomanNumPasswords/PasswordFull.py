import numpy as np

# set up dictionary of Roman numerals
# dictionary values correspond to number of characters in keys
numerals_lengths = {
	"I": 1,
	"II": 2,
	"III": 3,
	"IV": 2,
	"V": 1,
	"VI": 2,
	"VII": 3,
	"VIII": 4
	}
#MAX_NUM_LENGTH = 4

# password string for the problem
# might need to generate an array from this to make it work
password = "IIIVIIIVIIIVIII"
#password = "IIIIIIIIII"
l_pass = len(password)
# this will be filled in from right to left
combinations = np.zeros(l_pass+1)
# adding a single dummy combination of length 0 as a placeholder
combinations[l_pass] = 1

# helper method to check if a given Roman numeral could appear at a given spot in the string
# returns true or false
def numeral_match(password,k,i):
	lp = len(password)
	v = len(k)
	if i+v-1>lp:
		return False
	else:
		return (password[i:i+v] == k)

for i in range(l_pass-1,-1,-1):
	# iterate through keys of dictionary
	# see if key could be present in the password starting at character i
	# if so, add number of combinations at index i + v, where v is the corresponding value
	for k,v in numerals_lengths.items():
		if numeral_match(password,k,i):
			combinations[i] += combinations[i+v]

print(combinations)
print(f"Total combinations for password {password}: {combinations[0]}")