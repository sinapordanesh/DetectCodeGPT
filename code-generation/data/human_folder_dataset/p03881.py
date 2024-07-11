import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

P = [int(x) for x in readline().split()]
Q = [int(x) for x in readline().split()]

def tour_win_rate(x):
    if x<0: return 1000
    if x>1: return 1000
    # petrが、Pをx、Qを1-xで選ぶとする。
    return sum(max(p*x,q*(1-x)) for p,q in zip(P,Q))/100

from scipy.optimize import fmin

xopt = fmin(tour_win_rate,x0=0.5,disp=False,xtol=1e-10)[0]
print(tour_win_rate(xopt))