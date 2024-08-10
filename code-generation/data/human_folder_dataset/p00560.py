from heapq import heapify, heappop, heappush
N, M, K = map(int, input().split())
A, B, C = map(int, input().split())
T = int(input())
S = [int(input())-1 for i in range(M)]

def f(rt, rn):
    return min(rt // A, rn-1)

ans = 0
que = []
for i in range(M-1):
    s0 = S[i]; s1 = S[i+1]
    if B*s0 <= T:
        rt = T - B*s0; rn = s1-s0
        k = f(rt, rn)
        ans += k+1

        rt -= (k+1)*C; rn -= k+1
        k0 = f(rt, rn)

        if k0 >= 0:
            que.append((-k0, rt, rn))
if B*S[-1] <= T:
    ans += 1
heapify(que)

for i in range(K-M):
    if not que:
        break
    k, rt, rn = heappop(que); k = -k
    rt -= (k+1)*C; rn -= k+1
    ans += k+1

    k0 = f(rt, rn)
    if k0 >= 0:
        heappush(que, (-k0, rt, rn))
print(ans-1)

