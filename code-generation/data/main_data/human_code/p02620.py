def calcScore():
    for d in range(1, D + 1):
        id = t[d]  # この日に開催するコンテスト
        sinceLast[d][id] = 0
        score[d][id] = s[d][id]


        for i in range(1, 26 + 1):
            if i == id:  continue
            sinceLast[d][i] = sinceLast[d - 1][i] + 1
            score[d][i] = -c[i] * sinceLast[d][i]

    ans = 0
    for d in range(1, D + 1):
        ans += sum(score[d])

    return ans

def calcScoreDiff(score, d, before, after):
    ans = 0
    for dd in range(d, D + 1):
        if dd > d and t[dd] == before:  break
        sinceLast[dd][before] = sinceLast[dd - 1][before] + 1
        ans -= score[dd][before]
        score[dd][before] = -c[before] * sinceLast[dd][before]
        ans += score[dd][before]

    ans -= score[d][after]
    sinceLast[d][after] = 0
    score[d][after] = s[d][after]
    ans += score[d][after]

    for dd in range(d + 1, D + 1):
        if t[dd] == after:  break
        sinceLast[dd][after] = sinceLast[dd - 1][after] + 1
        ans -= score[dd][after]
        score[dd][after] = -c[after] * sinceLast[dd][after]
        ans += score[dd][after]

    return ans

D = int(input())
c = [0] + [int(x) for x in input().split()]
s = [[0 for _ in range(26 + 1)]] + \
    [[0] + [int(x) for x in input().split()] for _ in range(D)]
t = [0] + [int(input()) for _ in range(D)]

score = [[0] * (26 + 1) for _ in range(D + 1)]
sinceLast = [[0] * (26 + 1) for _ in range(D + 1)]
tot = calcScore()

M = int(input())
for i in range(M):
    d, after = [int(x) for x in input().split()]
    before = t[d]
    t[d] = after
    diff = calcScoreDiff(score, d, before, after)
    tot += diff
    print(tot)