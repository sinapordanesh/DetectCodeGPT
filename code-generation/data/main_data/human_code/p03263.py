H, W = map(int, input().split())
A = []
for i in range(H):
    r = list(map(int, input().split()))
    if i&1:
        r.reverse()
    A.append(r)

ans = []

for i in range(H*W-1):
    if A[i//W][i%W]&1:
        j = i+1
        A[j//W][j%W] += 1
        ans.append([i, j])

def f(n):
    x = n//W
    y = n%W
    if x&1:
        y = W-y-1
    return f"{x+1} {y+1}"

print(len(ans))
for a, b in ans:
    print(f(a), f(b))