import math
M = 256

def entropy_if_smallest(ctr,bound):
    ret = 0
    for v in ctr:
        if v == 0: continue
        ret -= (v / N) * math.log2(v / N)
        if ret >= bound:
            return None
    return ret

def solve(src):
    ans_h = float('inf')
    ans = None
    for s in range(16):
        for a in range(16):
            for c in range(16):
                ctr = [0] * M
                r = s
                for i in src:
                    r = (a*r + c) % M
                    o = (i + r) % M
                    ctr[o] += 1
                h = entropy_if_smallest(ctr,ans_h)
                if h is not None:
                    ans = (s,a,c)
                    ans_h = h
                    if ans_h == 0:
                        return ans
    return ans

while True:
    N = int(input())
    if N == 0: break
    src = list(map(int,input().split()))
    print(' '.join(map(str,solve(src))))