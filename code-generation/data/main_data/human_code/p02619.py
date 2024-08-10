D = int(input())
c = [0] + [int(x) for x in input().split()]
s = [[0 for _ in range(26 + 1)]] + \
    [[0] + [int(x) for x in input().split()] for _ in range(D)]
t = [0] + [int(input()) for _ in range(D)]

def calcScore():
    score = [[0] * (26 + 1) for _ in range(D + 1)]
    sinceLast = [[0] * (26 + 1) for _ in range(D + 1)]

    for d in range(1, D + 1):
        id = t[d]  # この日に開催するコンテスト
        sinceLast[d][id] = 0
        score[d][id] = s[d][id]


        for i in range(1, 26 + 1):
            if i == id:  continue
            sinceLast[d][i] = sinceLast[d - 1][i] + 1
            score[d][i] = -c[i] * sinceLast[d][i]

    total = sum(sum(row) for row in score)

    ans = 0
    for d in range(1, D + 1):
        ans += sum(score[d])
        print(ans)

    return ans

calcScore()