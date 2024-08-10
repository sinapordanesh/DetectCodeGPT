def resolve():
	n,r = map(int,input().split())
	print(r if n>=10 else r+100*(10-n))
resolve()