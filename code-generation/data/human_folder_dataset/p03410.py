import sys
from bisect import bisect_right,bisect_left
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
A,B = LI(),LI()

# 各桁の xor を考える

ans = 0
mod = 1 << 29
for i in range(29,0,-1):  # 2**(i-1) の位
    X = [a & (mod-1) for a in A]
    Y = [b & (mod-1) for b in B]
    X.sort()
    Y.sort(reverse=True)
    mod >>= 1
    r = 0
    i1,i2,i3 = 0,0,0
    for j in range(N):
        x = X[j]
        # [2**(i-1)-x,2*2**(i-1)-x),[3*2**(i-1)-x,4*2**(i-1)-x) にある Y の要素の個数を数え上げる
        # 尺取り法
        while i1 < N and Y[i1] >= mod-x:
            i1 += 1
        while i2 < N and Y[i2] >= 2*mod-x:
            i2 += 1
        while i3 < N and Y[i3] >= 3*mod-x:
            i3 += 1
        r += i1-i2+i3
    if r % 2 == 1:
        ans += mod

print(ans)
