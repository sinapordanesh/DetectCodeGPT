import sys
from itertools import accumulate


def input():
    return sys.stdin.readline().strip()


def acc(li, n):
    res = [0] * (n + 1)
    for i in range(n):
        if li[i] == "A":
            res[i + 1] = 1
        elif li[i] == "B":
            res[i + 1] = 2
    return list(accumulate(res))


def restore(x, y, li):
    return (li[y] - li[x - 1]) % 3


S = input()
T = input()
N = len(S)
M = len(T)

acc_S = acc(S, N)
acc_T = acc(T, M)

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    v_S = restore(a, b, acc_S)
    v_T = restore(c, d, acc_T)
    print("YES") if v_S == v_T else print("NO")
