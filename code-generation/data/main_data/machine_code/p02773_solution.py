from collections import Counter

def most_common_votes(N, votes):
    counter = Counter(votes)
    max_votes = max(counter.values())
    result = sorted([key for key, value in counter.items() if value == max_votes])
    for res in result:
        print(res)

# Input
N = int(input())
votes = [input() for _ in range(N)]

# Calling the function
most_common_votes(N, votes)