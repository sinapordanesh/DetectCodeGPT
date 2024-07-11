import sys
def input():
	return sys.stdin.buffer.readline()[:-1]
n = int(input())
men = [tuple(map(int, input().split())) for _ in range(n)]
men.sort(key=lambda x: (x[0]+x[1], -x[0]))
allowed = [-1 for _ in range(n)]
allowed[n-1] = men[-1][0]
for i in range(n-2, -1, -1):
	allowed[i] = max(allowed[i+1], men[i][0])

INF = 10**10
dp = [INF for _ in range(n+1)]
dp[0] = 0
for i in range(n):
	for j in range(i+1, 0, -1):
		if dp[j-1] <= men[i][0]:
			dp[j] = min(dp[j], dp[j-1] + men[i][1])

#print(dp)
for i in range(n+1):
	if dp[i] < INF:
		ans = i
print(ans)