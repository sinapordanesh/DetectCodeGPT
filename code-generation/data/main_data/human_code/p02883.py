import sys
input = sys.stdin.readline
MI=lambda:map(int,input().split())
LI=lambda:list(map(int,input().split()))

N,K=MI()
A=LI()
A.sort(reverse=True)
F=LI()
F.sort()

def check(x):
    # x分以内に食べきれるための修行回数はK回以下か
    k=0
    for i in range(N):
        k+=max(int(0--(A[i]-x//F[i])//1),0)
    return k<=K

    
ok=10**13
ng=-1
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if check(mid):
        ok=mid
    else:
        ng=mid
print(ok)