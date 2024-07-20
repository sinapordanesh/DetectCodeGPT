def is_keepable(size, sub, add, start):
    small, big = 1, size
    for i in range(N - 1, -1, -1):
        if T[i] == sub:
            big = min(big + 1, size)
        elif T[i] == add:
            small = max(small - 1, 1)
        if S[i] == sub:
            small += 1
        elif S[i] == add:
            big -= 1
        if small > big:
            return False
    return small <= start <= big


H, W, N = map(int, input().split())
sr, sc = map(int, input().split())
S = input()
T = input()
if is_keepable(H, "U", "D", sr) and is_keepable(W, "L", "R", sc):
    print("YES")
else:
    print("NO")
