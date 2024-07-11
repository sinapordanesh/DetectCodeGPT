def check(n):
    i = 1
    while n > 0:
        n -= i
        if n == 0:
            return i
        i += 1
    return 0


N = int(input())
K = check(N)
if K == 0:
    print("No")
    exit()

print("Yes")
print(K + 1)
ans = [[] for _ in range(K + 1)]
cur = 0
nxt = K
for k in range(K):
    ans[k] += range(cur + 1, cur + K - k + 1)
    for i in range(K - k):
        ans[i + k + 1].append(i + cur + 1)
    cur += nxt
    nxt -= 1

[print(K, *row) for row in ans]
