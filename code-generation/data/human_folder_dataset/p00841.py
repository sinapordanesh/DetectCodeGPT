def solve():
    from bisect import bisect
    from itertools import accumulate
    from sys import stdin
    f_i = stdin
    
    while True:
        n = int(f_i.readline())
        if n == 0:
            break
        
        a = list(map(int, f_i.readline().split()))
        b = float(f_i.readline())
        r, v, e, f = map(float, f_i.readline().split())
        
        r = int(r)
        a_n = a.pop()
        
        dp = [1 / (v - f * (r - x))for x in range(r)]
        dp += [1 / (v - e * (x - r))for x in range(r, a_n)]
        
        dp = list(accumulate(dp))
        cost = tuple(time + b for time in dp)
        
        for a_i in a:
            base = dp[a_i-1]
            for i, tpl in enumerate(zip(dp[a_i:], cost), start=a_i):
                pre, new = tpl
                new += base
                if new < pre:
                    dp[i] = new
        
        print(dp[-1])

solve()
