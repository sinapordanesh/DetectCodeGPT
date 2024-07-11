from functools import reduce

EPSILON = 1e-5
d = 0
Vs = []

times = lambda x,y: x*y

def interpolate(x, e):
    return sum(
        reduce(
            times, [(x-j)/(i-j) for j in range(len(Vs)) if j not in [i,x,e]]
            )*v for i,v in enumerate(Vs) if i not in [x,e])

def outlier(e):
    for i,v in enumerate(Vs):
        if i==e: continue
        if abs(interpolate(i,e) - v) < EPSILON: return False
    return True

def solve():
    for i in range(d+3):
        if not outlier(i): return i
    return -1

while True:
    d = int(input())
    if d==0: break
    Vs = [float(input()) for i in range(d+3)]
    print(solve())
