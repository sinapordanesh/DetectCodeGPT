def count_ways(N, K, S, T, A):
    count = 0
    for i in range(1, 1 << N):
        if bin(i).count('1') <= K:
            chosen = [A[j] for j in range(N) if (i >> j) & 1]
            if len(chosen) >= 1 and len(chosen) <= K and (reduce(lambda x, y: x & y, chosen) == S) and (reduce(lambda x, y: x | y, chosen) == T):
                count += 1
    return count

# Sample Input 1
print(count_ways(3, 3, 0, 3, [1, 2, 3]))

# Sample Input 2
print(count_ways(5, 3, 1, 7, [3, 4, 9, 1, 5]))

# Sample Input 3
print(count_ways(5, 4, 0, 15, [3, 4, 9, 1, 5]))