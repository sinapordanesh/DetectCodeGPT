def main():
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	A.sort()
	cnt = []
	c = 0
	a = 0
	for i in range(len(A)):
		if i == 0:
			a = A[i]
			c += 1
		else:
			if A[i] == a:
				c += 1
			elif A[i] != a:
				cnt.append(c)
				c = 1
				a = A[i]
	else:
		cnt.append(c)

	cnt = list(map(lambda ct: (2 - (ct % 2)), cnt))
	evens = cnt.count(2)
	if evens % 2 == 0:
		print(len(cnt))
	else:
		print(len(cnt) - 1)

main()