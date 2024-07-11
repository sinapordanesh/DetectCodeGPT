def distance(star, position):
    return sum([(a - b)**2 for a, b in zip(star, position)])**(1 / 2)


def difference(star, position):
    return [(a - b) for a, b in zip(star, position)]


while True:
    n = int(input())
    if n == 0:
        break
    stars = [list(map(float, input().split())) for i in range(n)]
    position = [sum([s[i] for s in stars]) / len(stars) for i in range(3)]
    move_rate = 1
    for i in range(3000):
        if i % 100 == 0:
            move_rate /= 2
        index = 0
        dis_max = 0
        for j, star in enumerate(stars):
            dis = distance(star, position)
            if dis_max < dis:
                dis_max = dis
                index = j
        diff = difference(stars[index], position)
        position = [(position[i] + diff[i] * move_rate) for i in range(3)]

    print(format(dis_max, ".5f"))
