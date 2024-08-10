s=list(map(int,list(input())))
# s[0]=1,s[-1]=0,s[k]=s[n-k-1]は必要
def main(s):
  n=len(s)
  if s[0]!=1 or s[-1]!=0:return [[-1]]
  for k in range(n//2-1):
    if s[k]!=s[n-k-2]:return [[-1]]
  uv=[(1,2)]
  t=2
  i=3
  for x in s[1:-1]:
    uv.append((t,i))
    if x==1:
      t=i
    i+=1
  return uv
for x in main(s):
  print(*x,sep=' ')
