def max_score(N, a):
    a.sort()
    score = sum(a[N:2*N]) - sum(a[:N])
    return score

# Sample Input 1
# N = 2
# a = [3, 1, 4, 1, 5, 9]
# Sample Output 1
# print(max_score(2, [3, 1, 4, 1, 5, 9]))

# Sample Input 2
# N = 1
# a = [1, 2, 3]
# Sample Output 2
# print(max_score(1, [1, 2, 3]))

# Sample Input 3
# N = 3
# a = [8, 2, 2, 7, 4, 6, 5, 3, 8]
# Sample Output 3
# print(max_score(3, [8, 2, 2, 7, 4, 6, 5, 3, 8]))