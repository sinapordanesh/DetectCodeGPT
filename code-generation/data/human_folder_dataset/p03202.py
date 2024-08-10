N=int(input())
A=list(map(int,input().split()))
def judge(X):
  Y=[[A[0],1]]
  Z=0
  for i in range(N-1):
    if A[i]<A[i+1]:
      Y.append([A[i+1]-A[i],1])
    else:
      Z=A[i]-A[i+1]
      for j in range(len(Y)):
        if Y[-1][0]<=Z:
          Z-=Y[-1][0]
          del Y[-1]
        else:
          Y[-1][0]-=Z
          break
      Z=0
      for j in range(len(Y)-1,-2,-1):
        if j==-1:
          return False
        if Y[j][1]==X or Y[j][0]==0:
          Z+=Y[j][0]
          del Y[j]
        else:
          if Y[j][0]==1:
            Y.append([1,Y[j][1]+1])
            del Y[j]
          else:
            Y[j][0]-=1
            Y.append([1,Y[j][1]+1])
          if Z:
            Y.append([Z,1])
          break
  return True

L,R,M=1,10**9,0
while R>L:
  M=(L+R)//2
  if judge(M):
    R=M
  else:
    L=max(L+1,M)
print(L)