import sys
S=sys.stdin.readlines()
def Binit(B,siz):
  while len(B)<siz+1:
    B.append(0)
  while len(B)>siz+1:
    del B[-1]
  for i in range(siz+1):
    B[i]=0
  B.append(siz)

def Badd(B,a,x):
  z=a
  while z<=B[-1]:
    B[z]+=x
    z+=(z&(-z))

def Bsum(B,a):
  r=0
  z=a
  while z>0:
    r+=B[z]
    z-=(z&(-z))
  return r

def Bssum(B,a,b):
  return Bsum(B,max(a,b))-Bsum(B,min(a,b)-1)

N=int(S[0])
X=[list(map(int,S[i+1].split())) for i in range(N)]
X.sort()
for i in range(N):
  X[i][0]=i
D=dict()
Y=sorted([X[i][1] for i in range(N)])
for i in range(N):
  D[Y[i]]=i
for i in range(N):
  X[i][1]=D[X[i][1]]
B1,B2=[],[]
Binit(B1,N+1)
Binit(B2,N+1)
for i in range(N):
  Badd(B2,i+1,1)
mod=998244353
P=N*pow(2,N-1,mod)%mod
Z=[[1,1,1,1],[1,1,1,0],[1,1,0,1],[1,0,1,1],[1,0,0,1],[0,1,1,1],[0,1,1,0]]
A=0
for i in range(N):
  Badd(B2,X[i][1]+1,-1)
  V=[Bsum(B1,X[i][1]+1),Bsum(B2,X[i][1]+1)]
  W=[pow(2,V[0],mod)-1,pow(2,i-V[0],mod)-1,pow(2,V[1],mod)-1,pow(2,N-i-1-V[1],mod)-1]
  for j in range(7):
    A=1
    if Z[j][0]:
      A=A*W[0]%mod
    if Z[j][1]:
      A=A*W[1]%mod
    if Z[j][2]:
      A=A*W[2]%mod
    if Z[j][3]:
      A=A*W[3]%mod
    P=(P+A)%mod
  Badd(B1,X[i][1]+1,1)
print(P)