def L():
    return list(map(int, input().split()))

[x,y]=L()

if x%y==0:
  print(-1)
else:
  print(x)
