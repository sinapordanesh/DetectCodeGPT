import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import product
def main():
    n, m = map(int, input().split())
    light_bulbs = {i: [] for i in range(m)}
    for i0 in range(m):
        data = tuple(map(int, input().split()))
        light_bulbs[i0]= data[1:]
    p = tuple(map(int, input().split()))

    pat = tuple(product((0, 1), repeat=n))
    res = 0
    for pate in pat:
        light_on = 0
        for i, bulb in enumerate(light_bulbs.values()):
            turned_switch = 0
            for bulb_switch in bulb:
                turned_switch += pate[bulb_switch - 1]
            if turned_switch % 2 == p[i]:
                light_on += 1
        if light_on == m:
            res += 1
    print(res)

if __name__ == '__main__':
    main()