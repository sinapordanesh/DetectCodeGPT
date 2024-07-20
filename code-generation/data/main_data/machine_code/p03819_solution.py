def railway_company(N, M, souvenirs):
    ans = [0] * (M+1)
    for i in range(1, M+1):
        for l, r in souvenirs:
            if l <= i <= r:
                ans[i] += 1
    return ans[1:]

# Sample Input
N = 3
M = 3
souvenirs = [(1, 2), (2, 3), (3, 3)]
print(*railway_company(N, M, souvenirs))

N = 7
M = 9
souvenirs = [(1, 7), (5, 9), (5, 7), (5, 9), (1, 1), (6, 8), (3, 4)]
print(*railway_company(N, M, souvenirs))