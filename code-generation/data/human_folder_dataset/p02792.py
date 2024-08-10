import math

def main():
	N = int(input())
	c = [[0] * 10 for i in range(10)]
	for i in range(1, N + 1):
		digit = int(math.log10(i)) + 1
		c[i // (10 ** (digit - 1))][i % 10] += 1

	cnt = 0
	for i in range(10):
		for j in range(10):
			cnt += c[i][j] * c[j][i]

	print(cnt)



main()