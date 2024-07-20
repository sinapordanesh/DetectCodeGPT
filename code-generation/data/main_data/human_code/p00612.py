# A106633
def f(n):
  res=1+2*n
  i=1
  while i*i<=n:
    res+=1+(n-i*i)//i*2
    i+=1
  return res

while 1:
  n=int(input())
  if n==0: break
  print(8*f(n//2-1)+8*n)