from itertools import permutations
import numpy as np

# 3 types of cards, each with 14 cards, plus 2 wild cards
cards_per_type = 14
n_types = 3
n_wild_cards = 2
n_cards = cards_per_type * n_types + n_wild_cards

def get_card_type(card_index):
    # regular card types are labeled as 0, 1, ..., (n_types - 1)
    # wild cards are type n_types
    # using minimum allows for case where n_wild_cards > cards_per_type
    return min(card_index // cards_per_type, n_types)

def set_exists(index_list):
    # using 0.5 and 2.5 to not take any chances with floating point errors
    if index_list[n_types] > 0.5:
        return True # has a wild card
    elif max(index_list) > 2.5:
        return True # has 3 of same type
    elif min(index_list[0:n_types]) > 0.5:
        return True # has one of every type
    else:
        return False

count = 44 * 43 * 42 * 41
total_cards_for_avg = 0
# Only looking at the first 4 cards because the 5th guarantees a set
for perm in list(permutations(range(n_cards), 4)):
    perm_types = np.zeros(n_types + 1)
    for i in range(3):
        perm_types[get_card_type(perm[i])] += 1
    if set_exists(perm_types):
        total_cards_for_avg += 3
    else:
        perm_types[get_card_type(perm[3])] += 1
        if set_exists(perm_types):
            total_cards_for_avg += 4
        else:
            total_cards_for_avg += 5

print(f"Average number of cards to get a set: {total_cards_for_avg/count}")