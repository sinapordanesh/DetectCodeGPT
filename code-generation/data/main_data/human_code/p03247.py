N=int(input())
X=[list(map(int,input().split())) for i in range(N)]
Y=set()
B=[[1,1] for i in range(N)]
for i in range(N):
  for j in range(2):
    if X[i][j]<0:
      B[i][j]=0
      X[i][j]*=-1
for i in range(N):
  Y.add(sum(X[i])&1)
if len(Y)==2:
  print(-1)
  exit()
Y=Y.pop()
def f(x):
  r=[]
  y=x
  for i in range(20):
    r.append(y%3)
    y//=3
  return r

P=[[] for i in range(N)]
if Y:
  print(39)
  print(*[3**(i//2) for i in range(39)],sep=' ')
else:
  print(40)
  print(*[3**(i//2) for i in range(40)],sep=' ')
Z=[[f(X[i][0]),f(X[i][1])] for i in range(N)]
V=0
for i in range(N):
  V=[0]*2
  for j in range(20):
    for k in range(2):
      Z[i][k][j]+=V[k]
      V[k]=Z[i][k][j]//3
      Z[i][k][j]%=3
    if Z[i][0][j]==0:
      if Z[i][1][j]==0:
        P[i].append('R')
        P[i].append('L')
      elif Z[i][1][j]==1:
        P[i].append('U')
        P[i].append('U')
        V[1]+=1
      else:
        P[i].append('D')
        P[i].append('D')
    elif Z[i][0][j]==1:
      if Z[i][1][j]==0:
        P[i].append('R')
        P[i].append('R')
        V[0]+=1
      elif Z[i][1][j]==1:
        P[i].append('D')
        P[i].append('L')
      else:
        P[i].append('L')
        P[i].append('U')
        V[1]+=1
    else:
      if Z[i][1][j]==0:
        P[i].append('L')
        P[i].append('L')
      elif Z[i][1][j]==1:
        P[i].append('D')
        P[i].append('R')
        V[0]+=1
      else:
        P[i].append('R')
        P[i].append('U')
        V[1]+=1
        V[0]+=1
    if j==18 and Y:
      break
  if Y:
    if V[0]:
      P[i].append('L')
    else:
      P[i].append('D')
for i in range(N):
  for j in range(len(P[0])):
    if P[i][j]=='L':
      if B[i][0]:
        P[i][j]='R'
    elif P[i][j]=='R':
      if B[i][0]:
        P[i][j]='L'
    elif P[i][j]=='U':
      if B[i][1]:
        P[i][j]='D'
    else:
      if B[i][1]:
        P[i][j]='U'
  print(*P[i],sep='')