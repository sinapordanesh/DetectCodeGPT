import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
INF = float("inf")
from heapq import heappop, heappush

def getlist():
	return list(map(int, input().split()))

def main():
	N = int(input())
	A = getlist()
	left = 0
	leftlis = [0] * (N + 1)
	rightlis = [0] * (N + 1)
	Q = []
	for i in range(N):
		left += A[i]
		heappush(Q, A[i])
	leftlis[0] = left

	for i in range(N, 2 * N):
		heappush(Q, A[i])
		left -= heappop(Q)
		left += A[i]
		leftlis[i + 1 - N] = left

	Q = []
	right = 0
	for i in range(3 * N - 1, 2 * N - 1, -1):
		right -= A[i]
		heappush(Q, -A[i])

	rightlis[0] = right

	for i in range(2 * N - 1, N - 1, -1):
		heappush(Q, -A[i])		
		right -= heappop(Q)
		right -= A[i]
		rightlis[2 * N - i] = right

	rightlis = list(reversed(rightlis))
	# print(leftlis)
	# print(rightlis)
	ans = -INF
	for i in range(N + 1):
		ans = max(ans, leftlis[i] + rightlis[i])

	print(ans)

if __name__ == '__main__':
	main()