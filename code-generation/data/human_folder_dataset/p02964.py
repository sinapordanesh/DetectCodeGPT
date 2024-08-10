import sys
input = sys.stdin.readline
from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))

#N = 2*10**5
#K = 10**12
#A = [(i % 200000) + 1 for i in range(N)]

def answer(N,K,A):
    s = []
    for i in range(N*K):
        a = A[i%N]
        if a in s:
            s = s[:s.index(a)]
        else:
            s.append(a)
    return s

def solve(N,K,A):
    B = A * 2
    NA = [-1]*N
    d = {}
    for i, b in enumerate(B):
        if b in d:
            if NA[d[b]%N] == -1:
                NA[d[b]%N] = i - d[b]+1
            d[b] = i 
        else:
            d[b] = i

    L = 57
    ds = [NA]
    for i in range(L):
        pre = ds[-1]
        temp = [pre[j] + pre[(pre[j]+j)%N] for j in range(N)]
        ds.append(temp)

    cnt = 0
    i = 0

    L -= 1
    NA = ds[L]
    while True:
        add = NA[i]
        nxt = ((i + add)%N)
        if cnt + add > N*K:
            L -= 1
            if L < 0:
                break
            NA = ds[L]
            continue
        cnt += add
        i = nxt


    s = []
    NA = ds[0]
    while cnt < N*K:
        a = A[i%N]
        add = NA[i%N]
        if add + cnt > N*K:
            s.append(a)
            i = (i+1) % N
            cnt += 1
        else:
            i = (i+add) % N
            cnt += add

    return s
print(*solve(N,K,A))

#import random
#N,K = 2*10**5,2*10**5
#A = [random.randint(1,2*10**5) for i in range(N)]
#solve(N,K,A)
#exit()
#for i in range(100):
#    import random
#    N,K = 100,100
#    A = [random.randint(1,10) for i in range(N)]
#    s1 = answer(N,K,A)
#    s2 = solve(N,K,A)
#    if s1 != s2:
#        print(N,K,A)
#        print(s1)
#        print(s2)
#        break
