import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K, C = mapint()
S = list(input())
r_S = S[::-1]

pos = [10**18]*N
neg = [10**18]*N
ok = 0
cnt = 0
for i in range(N):
    if S[i]=='o':
        if ok<=i:
            pos[i] = cnt + 1
            cnt += 1
            ok = i + C + 1

    else:
        pass
ok = 0
cnt = 0
for i in range(N):
    if r_S[i]=='o':
        if ok<=i:
            neg[i] = cnt + 1
            cnt += 1
            ok = i + C + 1

    else:
        pass

ans = []
neg = neg[::-1]

for i in range(N):
    if pos[i]+neg[i]-1==K:
        ans.append(i)
for a in ans:
    print(a+1)