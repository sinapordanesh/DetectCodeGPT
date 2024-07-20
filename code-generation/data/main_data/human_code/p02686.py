import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    first = []
    second = []

    for _ in range(N):
        s = input()
        l, r = 0, 0
        cnt = 0
        for char in s:
            if char == "(":
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    l += 1
        r = cnt
        if r >= l:
            first.append((l, r))
        elif l > r:
            second.append((l, r))

    from operator import itemgetter

    first.sort(key=itemgetter(0))
    second.sort(key=itemgetter(1), reverse=True)

    r_cur = 0

    for x, y in first:
        r_cur -= x
        if r_cur < 0:
            return print("No")
        r_cur += y

    for x, y in second:
        r_cur -= x
        if r_cur < 0:
            return print("No")
        r_cur += y

    if r_cur == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
