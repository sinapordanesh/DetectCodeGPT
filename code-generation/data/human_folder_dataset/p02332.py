import sys
sys.setrecursionlimit(10**6)

MOD = 1000000007

def main():
	n,k = map(int, input().split())
	if n > k:
		print(0)
	else:
		ans = 1
		for i in range(k,k-n,-1):
			ans *= i
			ans %= MOD
		print(ans)
	return

main()
