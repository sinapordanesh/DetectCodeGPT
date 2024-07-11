n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
def rui(A):
    R=[A[0]]*len(A)
    for i in range(len(A)-1):
        R[i+1]=R[i]+A[i+1]
    return R
R=rui(A)
RR=rui(B)
ans=0
for i in range(n):
    tt=RR[i-1] if i!=0 else 0
    ans=max(ans,R[i]+ RR[-1]-tt)
print(ans)