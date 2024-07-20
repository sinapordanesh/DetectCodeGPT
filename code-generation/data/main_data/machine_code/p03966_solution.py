def min_total_votes(N, votes):
    aoki = 1
    takahashi = 1
    
    for i in range(N):
        ratio = votes[i]
        mul = max((aoki + ratio[1] - 1) // ratio[1], (takahashi + ratio[0] - 1) // ratio[0])
        aoki = ratio[1] * mul
        takahashi = ratio[0] * mul
    
    return aoki + takahashi

# Sample Input 1
N = 3
votes = [(2, 3), (1, 1), (3, 2)]
print(min_total_votes(N, votes))

# Sample Input 2
N = 4
votes = [(1, 1), (1, 1), (1, 5), (1, 100)]
print(min_total_votes(N, votes))

# Sample Input 3
N = 5
votes = [(3, 10), (48, 17), (31, 199), (231, 23), (3, 2)]
print(min_total_votes(N, votes))