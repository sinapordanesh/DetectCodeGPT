def solve(a,b,c):
	ans = 0
	if (a&1) != (b&1) and (a&1) != (c&1):
		ans += 1
		b += 1
		c += 1
	elif (b&1) != (a&1) and (b&1) != (c&1):
		ans += 1
		a += 1
		c += 1
	elif (c&1) != (a&1) and (c&1) != (b&1):
		ans += 1
		a += 1
		b += 1

	return ans + (c-b)//2 + (c-a)//2

print(solve(*sorted(map(int,input().split()))))