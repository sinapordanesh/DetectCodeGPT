def read():
  return list(map(int,input().split()))

def calc(bs,ls,first):
  if sum(ls[0::2])!=bs.count(first) or sum(ls[1::2])!=bs.count(1-first):
    return float("inf")
  res=0
  i,j=0,0
  for k in range(0,len(ls),2):
    if k>0: i+=ls[k-1]
    for _ in range(ls[k]):
      j=bs.index(first,j)
      res+=abs(j-i)
      i+=1
      j+=1
  return res

while 1:
  try:
    n,m=read()
    bs=read()
    ls=read()
  except: break
  print(min(calc(bs,ls,i) for i in range(2)))