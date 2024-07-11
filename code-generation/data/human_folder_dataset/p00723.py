def solve(s):
	res = set([s])
	for split_at in range(1, len(s)):
		a = s[:split_at]
		b = s[split_at:]
		res.add(a[::-1] + b)
		res.add(a + b[::-1])
		res.add(a[::-1] + b[::-1])
		res.add(b + a)
		res.add(b[::-1] + a)
		res.add(b + a[::-1])
		res.add(b[::-1] + a[::-1])
	return len(res)

N = int(input())
for _ in range(N):
	print(solve(input()))

