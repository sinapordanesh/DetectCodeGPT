def max_pairs(N, A):
    pairs = 0
    for i in range(1, N+1):
        pairs += A[i-1] // 2
        if A[i-1] % 2 == 1 and i < N and A[i] > 0:
            pairs += 1
            A[i] -= 1
    return pairs

#Sample Input 1
print(max_pairs(4, [4, 0, 3, 2]))

#Sample Input 2
print(max_pairs(8, [2, 0, 1, 6, 0, 8, 2, 1]))