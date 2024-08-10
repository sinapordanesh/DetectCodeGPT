# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#n,*ab = map(int,read().split())

cnt = 0

def ask(n):
    print(f"? {n}")
    sys.stdout.flush()
    return input() == "Y"
"""

def ask(n):
    global cnt
    cnt += 1
    print(f"? {n}, cnt = {cnt}")
    if n <= N:
        return str(n) <= str(N)
    else:
        return str(n) > str(N)
"""


def ans(n):
    print(f"! {n}")
    sys.stdout.flush()


N = 901234567

ok = 10
ng = 1
while ok-ng > 1:
    mid = (ok+ng)//2
    if ask(mid*10**15-1): ok = mid
    else: ng = mid
    #print(ok,ng)

v = top = ng # 先頭桁

for _ in range(9):
    ok = 10
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng)//2
        
        r = 10*v+mid
        while r < 10**12: r *= 10
        r -= 1
        
        if ask(r): ok = mid
        else: ng = mid
        #print(ok,ng)
    v = v*10+ng

#print(v,"vvv")
        
while v%10==0:
    v //= 10


#print(v)

res = [ask(10**i) for i in range(10)]

if all(res):
    two = [ask(2*10**i) for i in range(10)]
    if all(two):
        ans(1)
    else:
        idx = two.index(True)
        ans(10**(idx))

else:
    idx = res.index(False) # 桁数
    while v < 10**(idx-1):
        v *= 10
    ans(v)    
    


