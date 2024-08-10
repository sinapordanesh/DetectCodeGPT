def main():
	N, A, B = [int(n) for n in input().split(" ")]
	X = [int(x) for x in input().split(" ")]
	D = []
	for i in range(1, len(X)):
		D.append(X[i] - X[i - 1])
	print(sum([min(A * d, B) for d in D]))

main()