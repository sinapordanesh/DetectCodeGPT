def dig(x):
	return sum([int(i) for i in str(x)])

n = int(input())
ans = 1e20
for a in range(1, n):
	b = n - a
	ans = min(ans, dig(a)+dig(b))
print(ans)