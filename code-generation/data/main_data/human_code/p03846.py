MOD=1e9+7

from collections import defaultdict
def check_even(c):
	ans=1
	d=defaultdict(int)
	for i in range(len(c)):
		d[c[i]]+=1
	
		if c[i]>=len(c) or c[i]%2==0 or d[c[i]]>2:
			return 0
		
		if d[c[i]]==1:
			ans=ans*2 % MOD
	return int(ans)
		
def check_odd(c):
	ans=1
	d=defaultdict(int)
	for i in range(len(c)):
		d[c[i]]+=1
		if c[i]>=len(c) or c[i]%2==1 or d[0]>1 or d[c[i]]>2:
			return 0
		
		if c[i]!=0 and d[c[i]]==1:
			ans=ans*2%MOD
			
	return int(ans)
		
n=int(input())
c=list(map(int,input().split()))
if n%2==0:
	print(check_even(c))
else:
	print(check_odd(c))
	
