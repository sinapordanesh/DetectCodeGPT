n, k = map(int, input().split())

a = list(map(int, input().split()))

ng = 0
ok = 10 ** 9 + 1

def check(x):
    cnt = 0
    for l in a:
        cnt += (l-1)//x
    return cnt <= k

while abs(ok-ng) > 1:
    m = (ok + ng) // 2
    if check(m):
        ok = m
    else:
        ng = m

print(ok)