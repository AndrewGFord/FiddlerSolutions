## Fiddler on the Proof, September 19, 2025

import itertools

# Gets the length of the longest increasing subsequence of a given list of numbers
def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    lis = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_length = max(lis)
    max_index = lis.index(max_length)

    subsequence = []
    while max_index != -1:
        subsequence.append(arr[max_index])
        max_index = prev[max_index]

    return max_length, subsequence[::-1]

group_sizes = range(1, 11)

for n in group_sizes:
    total_lengths = 0
    count = 0
    for perm in itertools.permutations(range(1, n + 1)):
        total_lengths += longest_increasing_subsequence(perm)[0]
        count += 1
    answer = total_lengths / count if count > 0 else 0
    print(f"Average length of the longest valid subsequence for group size {n}: {answer}")
