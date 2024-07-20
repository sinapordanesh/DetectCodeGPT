def num_permutations(N, K, P):
    count = 0
    for i in range(N-K+1):
        temp = P[i:i+K]
        temp.sort()
        if P[:i] + temp + P[i+K:] == list(range(N)):
            count += 1
    return count

# Sample Input 1
print(num_permutations(5, 3, [0, 2, 1, 4, 3]))

# Sample Input 2
print(num_permutations(4, 4, [0, 1, 2, 3]))

# Sample Input 3
print(num_permutations(10, 4, [2, 0, 1, 3, 7, 5, 4, 6, 8, 9]))