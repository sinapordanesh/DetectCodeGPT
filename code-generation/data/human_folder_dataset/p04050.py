import sys


def solve(n, m, arr):
    odds = []
    evens = []
    for a in arr:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)

    if len(odds) > 2:
        print('Impossible')
        return

    if len(odds) == 2:
        o1, o2 = odds
        aaa = [o1] + evens + [o2]
        bbb = [2] * (o1 // 2 + 1)
        bbb += evens
        bbb += [2] * (o2 // 2)

    elif len(odds) == 1:
        if odds[0] == 1:
            aaa = odds + evens
            bbb = evens + odds
        elif evens:
            aaa = odds + evens
            bbb = [odds[0] - 1] + evens[:-1] + [evens[-1] + 1]
        else:
            aaa = odds
            bbb = [odds[0] // 2, odds[0] // 2 + 1]

    else:
        aaa = evens
        bbb = [1] + evens[:-1] + [evens[-1] - 1]

    print(*aaa)
    print(len(bbb))
    print(*bbb)


n, m, *aaa = map(int, sys.stdin.buffer.read().split())
solve(n, m, aaa)
