import sys
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
from fractions import Fraction as frac  #frac(a,b)で正確なa/b
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

n,a,b=map(int,input().split())
A=sorted(list(map(int,input().split())))
print(sum(A[n-a:])/a)
q=A[n-a]
cnt=A.count(A[n-a])
kaku= n- biright(A,q)

def C(n, r ,mod=2**62):
    if n-r<r: r=n-r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k]) %mod

    return result % mod
ans=0
if cnt==1:
    print(1);exit()

if kaku==0:
    for i in range( a-kaku,min(b-kaku,cnt)+1 ):
        ans+=C(cnt,i)

else:
    ans=C(cnt,a-kaku)
print(ans)