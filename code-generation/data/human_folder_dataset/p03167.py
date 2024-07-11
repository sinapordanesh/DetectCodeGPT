from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    mod = 10**9 + 7
    h, w = map(int, input().split())

    dp = [0] * (w + 1)
    dp[1] = 1
    for _ in range(h):
        a = input()
        for i in range(w):
            if a[i] == '#':
                dp[i+1] = 0
            else:
                dp[i+1] += dp[i]
                dp[i+1] %= mod

    print(dp[w])

main()