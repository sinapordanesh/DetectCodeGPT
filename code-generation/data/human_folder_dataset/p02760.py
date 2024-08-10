def Judge(a):
  col=[]
  diag1=0
  diag2=0

  for i in range(3):
    if(a[i].count(0)==3):
      return 1
      break
    if(a[i][0]==0):
      col.append(0)
    if(a[i][1]==0):
      col.append(1)
    if(a[i][2]==0):
      col.append(2)
    if(a[i][i]==0):
      diag1+=1
    if(a[i][-(i+1)]==0):
      diag2+=1
  if(diag1==3 or diag2==3):
    return 1
  if(col.count(0)==3 or col.count(1)==3 or col.count(2)==3):
    return 1
  return 0


a=[]
for i in range(3):
  a.append(list(map(int,input().split())))
n=int(input())
for i in range(n):
  b=int(input())
  for j in range(3):
    for k in range(3):
      if(b==a[j][k]):
        a[j][k]=0
judge=Judge(a)
if(judge==1):
  print("Yes")
else:
  print("No")