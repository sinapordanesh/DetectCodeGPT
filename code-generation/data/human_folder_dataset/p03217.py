n,d = map(int,input().split())
num = [[0]*d for i in range(d)]
a = 0
for i in range(n):
  x,y = map(int,input().split())
  x %=d
  y%=d
  num[x][y] += 1
  a = max(a,num[x][y])
x=1
while x*x<a:
  x += 1
r = (x-1)*d
a = x-1
dai = d-1
syo = 0
anum = [[[0]*d for i in range(d)]for i in range(3)]
rui = [[[0]*(2*d+1) for i in range(2*d+1)]for i in range(3)]
for i in range(d):
  for j in range(d):
    z = num[i][j]
    if z > (a+1)**2:
      anum[0][i][j]=1
      anum[1][i][j]=1
      anum[2][i][j]=1
    elif z> a*(a+1):
      anum[1][i][j]=1
      anum[2][i][j]=1
    elif z > a*a:
      anum[1][i][j]=1
for x in range(3):
  for i in range(1,2*d+1):
    for j in range(1,2*d+1):
      rui[x][i][j]+=rui[x][i-1][j]+rui[x][i][j-1]-rui[x][i-1][j-1]+anum[x][(i-1)%d][(j-1)%d]
def cheak(kon):
  for i in range(1,d+1):
    for j in range(1,d+1):
      if rui[0][i+kon][j+kon] - rui[0][i - 1][j+kon] - rui[0][i+kon][j - 1] + rui[0][i - 1][j - 1]:
        continue
      if rui[1][i+d-1][j+d-1] - rui[1][i+kon+1 - 1][j+d-1] - rui[1][i+d-1][j+kon+1 - 1] + rui[1][i+kon+1 - 1][j+kon+1 - 1]:
        continue
      if rui[2][i+d-1][j+kon] - rui[2][i+kon+1 - 1][j+kon] - rui[2][i+d-1][j - 1] + rui[2][i+kon+1 - 1][j - 1]:
        continue
      if rui[2][i+kon][j+d-1] - rui[2][i - 1][j+d-1] - rui[2][i+kon][j+kon+1 - 1] + rui[2][i - 1][j+kon+1 - 1]:
        continue
      return 1
  return 0 
kon = (dai+syo)//2
while True:
  if dai-syo <= 1:
    if cheak(syo) == 1:
       dai = syo
    break
  kon = (dai+syo)//2
  c = cheak(kon)
  if c == 1:
    dai = kon
  else:
    syo = kon
print(dai+r)
