import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K = MI()

if N-2*K+1 < 0:
    print(-1)
    exit()

ANS = [[0]*3 for _ in range(N)]
for i in range(K+2*N,K+3*N):
    ANS[i-(K+2*N)][2] = i

if N % 2 == 0:
    for i in range(N//2):
        ANS[2*i][0] = K+i
        ANS[2*i][1] = K+N+(N//2)+i
        ANS[2*i+1][0] = K+(N//2)+i
        ANS[2*i+1][1] = K+N+i

else:
    for i in range(N//2):
        ANS[2*i][0] = K+i
        ANS[2*i][1] = K+N+(N//2)+i
        ANS[2*i+1][0] = K+(N//2)+1+i
        ANS[2*i+1][1] = K+N+i
    ANS[-1][0] = K+(N//2)
    ANS[-1][1] = K+(2*N-1)

for i in range(N):
    a,b,c = ANS[i]
    print(a,b,c)
