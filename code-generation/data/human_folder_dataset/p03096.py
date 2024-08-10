from collections import Counter


def main():
    n = int(input())
    c = [input()]
    for _ in range(n - 1):
        now = input()
        if now != c[-1]:
            c.append(now)
    mod = 10 ** 9 + 7
    memo = Counter(c)
    # memo[i] := 色がiであるような石jについてのdp[j]の値の合計値（適宜更新する）
    for k in memo.keys():
        memo[k] = 0
    dp = [0 for _ in range(2 * 10 ** 5 + 10)]
    dp[0] = 1
    for i in range(len(c)):
        dp[i + 1] += memo[c[i]] + dp[i]
        # それ以前のdp[i]通りに加えて，c[i] -- (0 <= j < i and c[i] == c[j])間の
        # memo[c[i]]通りの区間の両端を定めることができるから，この遷移式が成り立つ．
        memo[c[i]] += dp[i]
        dp[i + 1] %= mod
        memo[c[i]] %= mod
    print(dp[len(c)])


if __name__ == '__main__':
    main()
