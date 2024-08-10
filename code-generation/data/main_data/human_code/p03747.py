import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,L,T = MI()
q,r = T//L,T % L
A = []
a = 0  # 開始時点で、(時計回りの蟻の数)-(半時計まわりの蟻)
for i in range(N):
    x,w = MI()
    a += (-2)*w+3
    for j in range(-1,2):
        A.append(x+r*((-2)*w+3)+j*L)
A.sort()

print(*[A[N+(i+q*a)%N] % L for i in range(N)],sep='\n')
