def lexicographically_smallest_permutation(N, p):
    ans = []
    for i in range(N-1, 0, -2):
        ans.append(p[i])
    for i in range(0, N, 2):
        ans.append(p[i])
    return ' '.join(map(str, ans))