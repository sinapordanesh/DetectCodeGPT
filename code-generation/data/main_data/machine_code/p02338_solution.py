def balls_and_boxes(n, k):
    MOD = 10**9 + 7
    if n <= k:
        return 1
    else:
        return 0

n, k = map(int, input().split())
print(balls_and_boxes(n, k))