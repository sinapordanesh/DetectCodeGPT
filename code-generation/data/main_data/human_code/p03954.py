N=int(input())
a=list(map(int,input().split()))
def cond(n):
    L=(0,-1)
    for i in range(1,N):
        if a[i]>=n and a[i-1]>=n:
            L=(i,1)
        elif a[i]<n and a[i-1]<n:
            L=(i,0)

    R=(2*N-1,-1)
    for i in range(2*N-3,N-2,-1):
        if a[i]>=n and a[i+1]>=n:
            R=(i,1)
        elif a[i]<n and a[i+1]<n:
            R=(i,0)

    if L[1]==-1 and R[1]==-1:
        return a[0]>=n
    elif L[1]==-1:
        return R[1]==1
    elif R[1]==-1:
        return L[1]==1
    elif L[1]==R[1]:
        return R[1]==1
    else:
        if L[1]==0:
            return N-1-L[0]>R[0]-(N-1)
        else:
            return N-1-L[0]<R[0]-(N-1)


start=1
end=2*N-1
while end-start>1:
    test=(end+start)//2
    if cond(test):
        start=test
    else:
        end=test
if cond(end):
    print(end)
else:
    print(start)