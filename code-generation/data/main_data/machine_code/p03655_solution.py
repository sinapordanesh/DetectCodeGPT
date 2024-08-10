def good_touring_plans(X1, X2, X3, X4, X5, X6, Y1, Y2, Y3, Y4, Y5, Y6):
    MOD = 10**9 + 7
    x = min(X4 - X3 + 1, X6 - X5 + 1)
    y = min(Y4 - Y3 + 1, Y6 - Y5 + 1)
    ans = x * y % MOD
    return ans

X1, X2, X3, X4, X5, X6 = map(int, input().split())
Y1, Y2, Y3, Y4, Y5, Y6 = map(int, input().split())
print(good_touring_plans(X1, X2, X3, X4, X5, X6, Y1, Y2, Y3, Y4, Y5, Y6))