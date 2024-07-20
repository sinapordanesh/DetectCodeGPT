from collections import defaultdict
def main(n):
    m = n * 499 + 1
    dp =  defaultdict(list)
    dp[0] = [0, 0]
    for _ in range(n):
        ndp = defaultdict(lambda:[-1,-1])
        for key, value in dp.items():
            ndp[key] = value[:]
        p = int(input())
        a = -p % 1000
        if a >= 500:
            b = a - 500
            for j in dp.keys():
                if dp[j][0] < 0: continue
                tmp = ndp[j + b]
                if tmp[0] < dp[j][0] + 1:
                    tmp[0] = dp[j][0] + 1
                    tmp[1] = dp[j][1] + p
                elif tmp[0] == dp[j][0] + 1 and tmp[1] > dp[j][1] + p:
                    tmp[0] = dp[j][0] + 1
                    tmp[1] = dp[j][1] + p
        else:
            b = 500 - a % 500
            for j in dp.keys():
                if dp[j][0] < 0: continue
                tmp = ndp[j + a]
                if tmp[0] < dp[j][0]:
                    tmp[0] = dp[j][0]
                    tmp[1] = dp[j][1] + p
                elif tmp[0] == dp[j][0] and tmp[1] > dp[j][1] + p:
                    tmp[1] = dp[j][1] + p
                if j - b >= 0:
                    tmp = ndp[j - b]
                    if tmp[0] < dp[j][0] + 1:
                        tmp[0] = dp[j][0] + 1
                        tmp[1] = dp[j][1] + p
                    elif tmp[0] == dp[j][0] + 1 and tmp[1] > dp[j][1] + p:
                        tmp[1] = dp[j][1] + p
        dp = ndp
    ans = [0, 0]
    for n, c in dp.values():
        if n > ans[0]:
            ans = [n, c]
        elif n == ans[0] and c < ans[1]:
            ans = [n, c]
    print(*ans)

if __name__ == "__main__":
    while 1:
        n = int(input())
        if n:
            main(n)
        else:
            break

