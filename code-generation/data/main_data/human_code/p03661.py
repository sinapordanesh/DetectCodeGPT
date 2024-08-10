n=int(input())
A=list(map(int,input().split()))

def rui(A):
    R=[A[0]]*len(A)
    for i in range(len(A)-1):
        R[i+1]=R[i]+A[i+1]
    return R
R=rui(A)
S=sum(A)
ans=10**20
for i in range(n-1):
    a=R[i] ; b=S-a
    ans=min(ans, abs(a-b))
print(ans)