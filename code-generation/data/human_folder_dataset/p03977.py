def solve(N,D):
    N-=1
    if  (N)%2==0:
        return 127*N+D
    else:
        return 127*N+(127-D)
T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    print(solve(a,b))