import sys
from subprocess import Popen, PIPE
from itertools import groupby
from collections import Counter

def main():
    sys.stdin.readline()
    S = sys.stdin.read().split()
    T = []
    inv_dict = {}
    Factors = Popen(["factor"] + S, stdout=PIPE).communicate()[0].split(b"\n")
    for factors in Factors[:-1]:
        factors = map(int, factors.split()[1:])
        t = 1
        t_inv = 1
        for f, group in groupby(factors):
            n = len(list(group)) % 3
            if n == 1:
                t *= f
            elif n == 2:
                t_inv *= f
        t, t_inv = t * t_inv * t_inv, t * t * t_inv
        T.append(t)
        inv_dict[t] = t_inv

    counter_T = Counter(T)
    ans = 0
    for t, t_cnt in counter_T.items():
        if t == 1:
            ans += 1
            continue
        t_inv = inv_dict[t]
        t_inv_cnt = counter_T[t_inv]
        if t_cnt > t_inv_cnt or (t_cnt == t_inv_cnt and t > t_inv):
            ans += t_cnt
    print(ans)

main()
