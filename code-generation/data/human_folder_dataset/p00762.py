#! cat input | python3 main.py
def debug():
    for X in field[size//2:] + field[:size//2]:
        print(X[size//2:], X[:size//2])

dice_data = [[],
        [4, 2, 3, 5],
        [4, 6, 3, 1],
        [6, 5, 1, 2],
        [1, 5, 6, 2],
        [4, 1, 3, 6],
        [4, 5, 3, 2],
        ]
def dice(t, f):
    i = dice_data[t].index(f)
    return [dice_data[t][x%4] for x in range(i, i + 4)]

size = 6
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def drop(t, f, nowl, nowr):
    target = list(map(lambda x: x > 3, dice(t, f)))
    now = [nowl, nowr]
    
    now_field = field[now[0]][now[1]]
    for i, tg in enumerate(target):
        if tg:
            nb_field = field[now[0] + move[i][0]][now[1] + move[i][1]]
            if nb_field[1] >= now_field[1]:
                target[i] = False
    for i, v in sorted(enumerate(dice(t, f)), key=lambda x: x[1], reverse=True):
        if target[i]:
            if i == 0:
                f = t
            elif i == 2:
                f = 7 - t
            t = 7 - v
            drop(t, f, now[0] + move[i][0], now[1] + move[i][1])
            break
    else:
        change = field[now[0]][now[1]]
        change[0] = t
        change[1] += 1

while True:
    n = int(input())
    if not n: break
    field = [[[0, 0] for i in range(size)] for j in range(size)]

    tfs = [list(map(int, input().split())) for x in range(n)]
    for t, f in tfs:
        drop(t, f, 0, 0)
    cnt = [0 for x in range(7)]
    for row in field:
        for cell in row:
            cnt[cell[0]] += 1
    print(*cnt[1:])