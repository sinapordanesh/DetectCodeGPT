n=int(input())
ar=3
sv=[0]*(10**6+2)
for i in range(2,len(sv)):
	if not sv[i]:
		sv[i]=i
		for j in range(2*i,len(sv),i):
			sv[j]=i
def di(x):
  an=1
  if sv[x]==x:
    return 2
  while x>1:
    ct=0;cr=sv[x]
    while x%cr==0:
      ct+=1;x//=cr
    an*=(ct+1)
  return an
for i in range(4,n+1):
  ar=ar+di(i-1)
if n==2:
  ar=1
print(ar)
