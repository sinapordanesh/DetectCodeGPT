def isqrt(n):
	L = 0
	R = n
	while R-L > 2:
		M = (L+R)//2
		if M*M==n:
			return M
		elif M*M < n:
			L = M
		else:
			R = M 
	for ans in range(R,L-1,-1):
		if ans*ans <= n:
			return ans
	assert(False)
	return -1
def count(n,A,B):
	ans = 0

	limit = isqrt(n)
	# x = A + 1
	# while True:
	# 	if x*x <= n:
	# 		if n//x < B:
	# 			ans += 1
	# 		x += 1
	# 	else:
	# 		return ans + min(n//x,B-1)
	return max(0,limit-A) + min(n//(limit+1),B-1)
for _ in range(int(input())):
	A, B = map(int,input().split())
	print(count(A*B-1,A,B)+count(A*B-1,B,A))