import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, k = input_int_list()
    ans = 0
    if k % 2 == 0:
        # a,b,c == k//2 + p*k を満たすとき
        cnt = ((n - (k // 2)) // k) + 1
        ans += pow(cnt, 3)

    # a,b,c == p*k を満たすとき
    ans += pow(n // k, 3)

    print(ans)

    return


if __name__ == "__main__":
    main()
