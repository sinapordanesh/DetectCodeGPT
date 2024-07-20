from sys import setrecursionlimit
setrecursionlimit(10**8)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[[-1] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 0.0

    def search(i, j, k):
        num = n
        if i > 0:
            if dp[i-1][j][k] == -1:
                num += search(i-1, j, k) * i
            else:
                num += dp[i-1][j][k] * i
        if j > 0:
            if dp[i+1][j-1][k] == -1:
                num += search(i+1, j-1, k) * j
            else:
                num += dp[i+1][j-1][k] * j
        if k > 0:
            if dp[i][j+1][k-1] == -1:
                num += search(i, j+1, k-1) * k
            else:
                num += dp[i][j+1][k-1] * k
        num /= i + j + k

        dp[i][j][k] = num
        return num

    print(search(a.count(1), a.count(2), a.count(3)))

main()