import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import Counter
    n = input_int()
    cnts = Counter(input_int_list())
    MOD = 10**9 + 7
    # nが奇数/偶数の場合で分ける
    if n % 2 == 1:
        # 0 が１人つ残りは、2,4,6... が2人ずついるはず
        if cnts[0] != 1:
            print(0)
            return
        for i in range(2, n - 1, 2):
            if cnts[i] != 2:
                print(0)
                return
    else:
        #  1,3,5... が2人ずついるはず
        for i in range(1, n, 2):
            if cnts[i] != 2:
                print(0)
                return
    print(pow(2, n // 2, MOD))
    return


if __name__ == "__main__":
    main()
