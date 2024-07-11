# 多くても 3 つがぎりぎり焼ける位置
from math import acos
from cmath import exp
from itertools import combinations
N, K = map(int, input().split())
XYC = []
for _ in range(N):
    x, y, c = map(int, input().split())
    XYC.append((complex(x, y), c))
if K==1:
    print(0)
    exit()
ans = 1e300
eps = 1e-7
for (p1, c1), (p2, c2) in combinations(XYC, 2):
    p_center = (p1 * c1 + p2 * c2) / (c1 + c2)
    t = abs(p_center-p1) * c1
    k = 0
    for xy, c in XYC:
        if abs(p_center-xy) * c < t + eps:
            k += 1
    if k >= K and t < ans:
        ans = t

def get_center(p1, p2, p3, c1, c2, c3):
    if c1 == c2 == c3:
        t1, t2, t3 = p2-p3, p3-p1, p1-p2
        denom = (t1*p1.conjugate()+t2*p2.conjugate()+t3*p3.conjugate())
        if denom == 0:
            return []
        return [(t1*abs(p1)**2+t2*abs(p2)**2+t3*abs(p3)**2) / denom]
    elif c1 == c3:
        c2, c3 = c3, c2
        p2, p3 = p3, p2
    elif c2 == c3:
        c1, c3 = c3, c1
        p1, p3 = p3, p1
    o1 = (c1*c1*p1-c3*c3*p3)/(c1*c1-c3*c3)
    r1 = (c1*c3*abs(p1-p3))/abs(c1*c1-c3*c3)
    o2 = (c2*c2*p2-c3*c3*p3)/(c2*c2-c3*c3)
    r2 = (c2*c3*abs(p2-p3))/abs(c2*c2-c3*c3)
    l = abs(o1-o2)
    if r1+r2 < l or l+r1<r2 or l+r2<r1:
        return []
    cos_a = (r1*r1+l*l-r2*r2)/(2*r1*l)
    a = acos(cos_a)
    res1 = o1 + (o2-o1) * exp(a*1j) * r1 / l
    res2 = o1 + (o2-o1) * exp(-a*1j) * r1 / l
    return [res1, res2]

for (p1, c1), (p2, c2), (p3, c3) in combinations(XYC, 3):
    p_centers = get_center(p1, p2, p3, c1, c2, c3)
    for p_center in p_centers:
        t = abs(p1 - p_center) * c1
        # print(abs(p1 - p_center) * c1,
        #       abs(p2 - p_center) * c2,
        #       abs(p3 - p_center) * c3)
        k = 0
        for p, c in XYC:
            if abs(p_center - p) * c < t + eps:
                k += 1
        if k >= K and t < ans:
            ans = t

print(ans)
