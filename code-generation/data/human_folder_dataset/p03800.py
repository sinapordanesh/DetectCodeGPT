# https://atcoder.jp/contests/arc069/tasks/arc069_b

from collections import deque

N = int(input())
S = input()

# 両方試すかな？ (1が羊(0)のとき，1が狼(1)のとき)
def valid(ans):
    # print(ans)
    for i in range(1, N - 1):
        if S[i] == 'o':
            if ans[i] == 0:
                ans[i + 1] = ans[i - 1]
            else:
                ans[i + 1] = 1 - ans[i - 1]
        else:
            if ans[i] == 0:
                ans[i + 1] = 1 - ans[i - 1]
            else:
                ans[i + 1] = ans[i - 1]

    flag1 = False
    if ans[-1] == 0:
        if S[-1] == 'o':
            flag1 = ans[-2] == ans[0]
        else:
            flag1 = ans[-2] != ans[0]
    else:
        if S[-1] == 'o':
            flag1 = ans[-2] != ans[0]
        else:
            flag1 = ans[-2] == ans[0]

    flag2 = False
    if ans[0] == 0:
        if S[0] == 'o':
            flag2 = ans[1] == ans[-1]
        else:
            flag2 = ans[1] != ans[-1]
    else:
        if S[0] == 'o':
            flag2 = ans[1] != ans[-1]
        else:
            flag2 = ans[1] == ans[-1]
    return flag1 and flag2

for (v0, v1) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    ans = [-1] * N
    ans[0] = v0
    ans[1] = v1
    flag = valid(ans)
    # print(ans, flag)
    if flag:
        for ch in ans:
            print('S' if ch == 0 else 'W', end='')
        print()
        exit()

print("-1")