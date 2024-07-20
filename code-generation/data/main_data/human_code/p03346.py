# https://atcoder.jp/contests/agc024/tasks/agc024_b
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    # 入力
    n = input_int()
    dp = [0] * (n + 1)
    # 解法 -> 最長の連続部分列を求めればよい
    # {1,3,4,5,2,7,6} => {3,4,5}

    for _ in range(n):
        a = input_int()
        dp[a] = dp[a - 1] + 1

    ans = n - max(dp)
    print(ans)

    return


if __name__ == "__main__":
    main()
