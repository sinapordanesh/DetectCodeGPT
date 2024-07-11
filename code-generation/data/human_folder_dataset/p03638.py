def main():
	H, W = [int(x) for x in input().split(" ")]
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	c = [[0] * W for i in range(H)]
	k = 0
	for i in range(len(c)):
		for j in range(len(c[i])):
			if i % 2 == 0:
				c[i][j] = str(k + 1)
				A[k] -= 1
			elif i % 2 == 1:
				c[i][-j-1] = str(k + 1)
				A[k] -= 1
			if A[k] == 0:
				k += 1
	print("\n".join([" ".join(ci) for ci in c]))

main()