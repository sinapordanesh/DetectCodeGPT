from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	H, W = getlist()
	L = []
	for i in range(H):
		l = list(input())
		L.append(l)

	redTable = [["."] * W for i in range(H)]
	blueTable = [["."] * W for i in range(H)]
	for i in range(H):
		redTable[i][0] = "#"
		blueTable[i][-1] = "#"

	for i in range(H):
		if i % 2 == 0:
			for j in range(1, W - 1):
				redTable[i][j] = "#"
		else:
			for j in range(1, W - 1):
				blueTable[i][j] = "#"

	# for i in range(H):
	# 	print(*redTable[i])
	# print()
	# for i in range(H):
	# 	print(*blueTable[i])

	for i in range(H):
		for j in range(1, W - 1):
			if L[i][j] == "#":
				if i % 2 == 0:
					blueTable[i][j] = "#"
				else:
					redTable[i][j] = "#"

	for i in range(H):
		print("".join(redTable[i]))
	print()
	for i in range(H):
		print("".join(blueTable[i]))

if __name__ == '__main__':
	main()