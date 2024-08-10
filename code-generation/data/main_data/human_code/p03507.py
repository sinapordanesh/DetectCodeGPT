# Atcoder problem Solving

# Code Festival Team Relay
import math

N, K = map(int, input().split())
que = [tuple(map(int, input().split())) for _ in range(N)]


def count(X):
    cnt = 0
    for i in range(N):
        w, d = que[i]
        if X >= w:
            cnt+=(X-w)//d+1
    return cnt


# case_impossible
l = -1

# case_possible

r = 10**19

while r-l > 1:
    m = (l+r)//2
    if count(m) < K:
        l = m
    else:
        r = m

print(r)