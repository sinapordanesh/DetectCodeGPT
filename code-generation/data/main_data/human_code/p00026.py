#!/usr/bin/python

paper = [[0] * 10 for i in range(10)]

def small(x, y):
    p = [[x, y]]
    for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        p.append([x + i, y + j])
    return p

def middle(x, y):
    p = small(x, y)
    for i, j in zip([1, -1, 1, -1], [1, 1, -1, -1]):
        p.append([x + i, y + j])
    return p

def big(x, y):
    p = middle(x, y)
    for i, j in zip([-2, 0, 2, 0], [0, -2, 0, 2]):
        p.append([x + i, y + j])
    return p

while True:
    try:
        x, y, size = map(int, input().split(','))
    except:
        break

    if size == 1:
        bp = small(x, y)
    elif size == 2:
        bp = middle(x, y)
    elif size == 3:
        bp = big(x, y)
    for p in bp:
        if 0 <= p[0] < 10 and 0 <= p[1] < 10:
            paper[p[1]][p[0]] += 1

print(sum(paper[y][x] == 0 for y in range(10) for x in range(10)))
print(max(paper[y][x] for y in range(10) for x in range(10)))