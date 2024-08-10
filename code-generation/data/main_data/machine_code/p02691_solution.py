def spy_party(N, A):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(i-j) == A[i] + A[j]:
                count += 1
    return count

# Sample Input 1
print(spy_party(6, [2, 3, 3, 1, 3, 1])) # 3

# Sample Input 2
print(spy_party(6, [5, 2, 4, 2, 8, 8])) # 0

# Sample Input 3
print(spy_party(32, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5])) # 22