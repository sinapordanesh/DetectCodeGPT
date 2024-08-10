n=int(input())
C=[]
S=[]
F=[]
for i in range(n-1):
	c,s,f=map(int, input().split())
	C.append(c)
	S.append(s)
	F.append(f)

def d(x,t): #駅x時間ｔで移動するのにかかる時間
	if S[x]>=t:
		return C[x]+S[x]-t
	else:
		if (t-S[x])%F[x]==0:
			return C[x]
		else:
			return C[x]+F[x]-(t-S[x])%F[x]

for i in range(n-1):
	x=i
	ans=0
	for j in range(x,n-1):
		ans+=d(j,ans)
		x=+1
	print(ans)
print(0)
