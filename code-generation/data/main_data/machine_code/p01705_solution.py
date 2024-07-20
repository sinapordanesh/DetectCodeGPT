import sys
from math import sqrt

def largest_square():
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        circles = []
        for _ in range(n):
            x, r = map(int, input().split())
            circles.append((x, r))
        
        max_side = 0
        for i in range(n-1):
            d = circles[i+1][0] - circles[i][0] - circles[i][1] - circles[i+1][1]
            side = min(d/2, circles[i][1], circles[i+1][1])
            max_side = max(max_side, side)
        
        print("{:.15f}".format(max_side*2))

largest_square()