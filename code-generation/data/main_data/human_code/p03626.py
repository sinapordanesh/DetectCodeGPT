def main():
	N = int(input())
	S1 = input()
	S2 = input()
	p = 1000000007
	dominoes = []
	pattern = 0
	i = 0
	while i < N:
		if S1[i] == S2[i]:
			if len(dominoes) == 0:
				pattern = 3
			elif dominoes[-1] == "|":
				pattern = (pattern * 2) % p
			elif dominoes[-1] == "-":
				pattern = (pattern * 1) % p
			dominoes.append("|")
			i += 1
		else:
			if len(dominoes) == 0:
				pattern = 6
			elif dominoes[-1] == "|":
				pattern = (pattern * 2) % p
			elif dominoes[-1] == "-":
				pattern = (pattern * 3) % p
			dominoes.append("-")
			i += 2
	print(pattern)

main()