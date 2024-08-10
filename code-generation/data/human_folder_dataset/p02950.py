#fin=open('in','r')
#input=lambda:fin.readline().strip()

p=int(input())
fact=[0]*p
inv=[0]*p
def f(x,m=p-2):
	ans=1
	while m:
		if m&1:ans=ans*x%p
		x=x*x%p
		m>>=1
	return ans
fact[0]=inv[0]=1
for i in range(1,p):
	fact[i]=fact[i-1]*i%p
	inv[i]=inv[i-1]*f(i)%p
r=list(map(int,input().split()))
c=[i for i in range(p) if r[i] == 1]
#sum of -((x-j)^(p-1)-1)
# (-j + x)^(p-1) = sum((-j)^i * x^(p-1-i) * binom(p-1,i))
coeff=[0]*p
for j in c:
	for i in range(p-1,-1,-1):
		if i&1:coeff[p-1-i]+=fact[p-1]*inv[i]*inv[p-1-i]*f(j,i)%p
		else:coeff[p-1-i]-=fact[p-1]*inv[i]*inv[p-1-i]*f(j,i)%p
	coeff[0]+=1
coeff=[(t%p+p)%p for t in coeff]
print(*coeff)