N,X=map(int,input().split())
t=[]
s=0
for i in range(N):
    b,l,u=map(int,input().split())
    t.append(((X-b)*u+l*b,b,l,u))
    s-=b*l
t.sort()
def condition(q):
    check=sum(t[i][0] for i in range(N-q,N))
    return check+s>=0

start=0
end=N
while end-start>1:
    test=(end+start)//2
    if not condition(test):
        start=test
    else:
        end=test

if not condition(end):
    Q=end
else:
    Q=start

check=sum(t[i][0] for i in range(N-Q,N))
check2=check+t[N-Q-1][0]
def condition2(r):
    M=0
    for i in range(N):
        test=0
        if N-Q>i:
            test=check
            val,b,l,u=t[i]
            if b>=r:
                test+=r*l
            else:
                test+=r*u-b*(u-l)
            M=max(M,test)
        else:
            val,b,l,u=t[i]
            test=check2-val
            if b>=r:
                test+=r*l
            else:
                test+=r*u-b*(u-l)
            M=max(M,test)
    return M+s>=0

start=0
end=X-1
while end-start>1:
    mid=(end+start)//2
    if condition2(mid):
        end=mid
    else:
        start=mid

if condition2(start):
    R=start
elif condition2(end):
    R=end
else:
    R=X
print(Q*X+R)