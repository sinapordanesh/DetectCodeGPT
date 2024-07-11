def perpro(q,p):
    res=[-1]*len(p)
    for i in range(len(p)):
        res[i]=q[p[i]]
    return res

def inverse(p):
    res=[-1]*len(p)
    for i in range(len(p)):
        res[p[i]]=i
    return res

N,K=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

ide_ele=[i for i in range(N)]

for i in range(N):
    p[i]-=1
    q[i]-=1

invp=[-1]*N
for i in range(N):
    invp[p[i]]=i

invq=[-1]*N
for i in range(N):
    invq[q[i]]=i

A=perpro(q,perpro(invp,perpro(invq,p)))

kthA=[A]
for i in range(30):
    kthA.append(perpro(kthA[-1],kthA[-1]))

def _nthA(n):
    res=ide_ele
    for i in range(30):
        if n>>i&1==1:
            res=perpro(res,kthA[i])
    return res

def ntha(n):
    qqq=n//4
    r=n%4
    if r==0:
        return _nthA(qqq)
    elif r==1:
        return perpro(_nthA(qqq),q)
    elif r==2:
        return perpro(_nthA(qqq),perpro(q,invp))
    else:
        return perpro(_nthA(qqq),perpro(q,perpro(invp,invq)))

Q=(K-1)//3
r=(K-1)%3
ans=[]
if Q==0:
    if K==1:
        ans=p
    elif K==2:
        ans=q
    else:
        ans=perpro(q,invp)
else:
    if Q%2==0:
        if r==0:
            mid=p
            a=ntha(2*Q-1)
            ans=perpro(a,perpro(mid,inverse(a)))
        elif r==1:
            mid=q
            a=ntha(2*Q)
            ans=perpro(a,perpro(mid,inverse(a)))
        else:
            mid=perpro(q,invp)
            a=ntha(2*Q)
            ans=perpro(a,perpro(mid,inverse(a)))
    else:
        if r==0:
            mid=invp
            a=ntha(2*Q-1)
            ans=perpro(a,perpro(mid,inverse(a)))
        elif r==1:
            mid=invq
            a=ntha(2*Q)
            ans=perpro(a,perpro(mid,inverse(a)))
        else:
            mid=perpro(invq,p)
            a=ntha(2*Q)
            ans=perpro(a,perpro(mid,inverse(a)))

for i in range(N):
    ans[i]+=1

print(*ans)