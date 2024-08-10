import math
import sys

def speed(floor):
    N = 5 * floor - 5
    time = math.sqrt(N/4.9)
    return (9.8 * time)

for s in sys.stdin:
    brkSpd = float(s)

    floor = 1

    while brkSpd > speed(floor):
        floor = floor + 1

    print(floor)