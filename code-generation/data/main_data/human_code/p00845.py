import math


def solve_cos(star, telescope):
    inner = sum([i * j for i, j in zip(star, telescope)])
    dis_star = (sum(map(lambda a: a * a, star)))**(1 / 2)
    dis_telescope = (sum(map(lambda a: a * a, telescope)))**(1 / 2)
    return inner / (dis_star * dis_telescope)


while True:
    n = int(input())
    if n == 0:
        break
    stars = [list(map(float, input().split())) for i in range(n)]
    m = int(input())
    telescopes = [list(map(float, input().split())) for i in range(m)]

    count = 0
    for star in stars:
        for telescope in telescopes:
            cos1 = solve_cos(star, telescope[:-1])
            cos2 = math.cos(telescope[-1])
            if cos2 <= cos1:
                count += 1
                break

    print(count)
