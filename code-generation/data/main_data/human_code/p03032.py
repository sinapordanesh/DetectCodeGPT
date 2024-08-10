# ABC128 D
from collections import deque

N,K=map(int,input().split())
V=list(map(int,input().split()))
V=V[:]+V[:]
def check(k):
    res=0
    # 連続する k(K,K-1,...)個の宝石をとる
    # K-k個まで捨ててよい
    for i in range(k+1):
        if k<N:
            v=V[N-k+i:N-k+i+k]
        else:
            v=V[:N]
        v.sort(reverse=True)
        for i in range(K-k):
            if not v:
                break
            if v[-1]<0:
                v.pop()
            else:
                break
        res=max(res,sum(v))
        if not k<N:
            break
    return res

res=0
for k in range(min(N,K)+1):
    res=max(res,check(k))
print(res)