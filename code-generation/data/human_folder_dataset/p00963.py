from math import cos, sin, pi, sqrt
B = ["BC", "CD", "DB"]
XY0, d0, l0, XY1, d1, l1 = open(0).read().split()
d0, l0, d1, l1 = map(int, [d0, l0, d1, l1])

def calc(XY, d, l):
    angle = B.index(XY) * 60 + d
    x = l * cos(pi*angle/180)
    y = l * sin(pi*angle/180)
    x = x + y/sqrt(3)
    y = y * 2/sqrt(3)
    x = x%2; y = y%2
    A = [["AC", "BD"], ["DB", "CA"]][int(x)][int(y)]
    return A[x%1>y%1]
print("YES"*(calc(XY0, d0, l0)==calc(XY1, d1, l1))or"NO")