import sys
from typing import List, Tuple

def last_moment_sun_blocked(r: int, n: int, buildings: List[Tuple[int, int, int]]) -> float:
    buildings.sort()
    max_height = 0
    last_moment = 0
    
    for i in range(len(buildings)):
        left, right, height = buildings[i]
        if height >= max_height:
            if right - left >= 2*r:
                last_moment = max(last_moment, (height - r) / 1)
            else:
                last_moment = max(last_moment, (height - r) / 1 + (2 * r - (right - left)) / 2)
            max_height = height
    
    return last_moment

for line in sys.stdin:
    r, n = map(int, line.strip().split())
    if r == 0 and n == 0:
        break
    buildings = []
    for _ in range(n):
        x_l, x_r, h = map(int, input().split())
        buildings.append((x_l, x_r, h))
    
    result = last_moment_sun_blocked(r, n, buildings)
    print("{:.4f}".format(result))