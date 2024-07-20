def floor_linear_sum(n,m,a,b):
    """
    returns sum((a*i+b)//m for i in range(n))
    """
    res = 0
    while True:
        if a >= m:
            res += (n-1)*n*(a//m)//2
            a %= m
        if b >= m:
            res += n * (b//m)
            b %= m

        y_max = (a*n+b)//m
        if y_max == 0:
            return res
        nx_max = b - y_max*m
        res += (n + nx_max//a)*y_max
        n,m,a,b = y_max, a, m, nx_max%a

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

T = int(readline())
m = map(int,read().split())
for t in zip(m,m,m,m):
    print(floor_linear_sum(*t))
