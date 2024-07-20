
"""

https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_e

ページの合計に与える寄与を考えればよい
ある位置iにある数字の与える寄与は
(自分より右にある数字の数)! * 自分より右にあるより小さい数字の数

元からおかれている数字同士に関しての寄与はBITで終わり
元からおかれている数字 & 自由な数字の寄与は
順列の総数 * 自由な数字の中で自分より小さいものの数 * 右にある空欄の数 / 全ての空欄の数 * fac[N-1-i]
順列の総数 * 自由な数字の中で自分より大きいものの数 * 左にある空欄の数 / 全ての空欄の数 * fac[N-1-i]
で求まる

自由同士は、半分になるはずなので
fac[N-1-i] * 右にある0の数 // 2
それより左にあるfacの平均を出す？→avrage
順列の総数 * 自由な数字の中で自分より大きいものの数 * 左にある空欄の数 / 全ての空欄の数 * average

"""

mod = 10**9+7
#逆元
def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2,mod)

#modのn!と、n!の逆元を格納したリストを返す(拾いもの)
#factorialsには[1, 1!%mod , 2!%mod , 6!%mod… , n!%mod] が入っている
#invsには↑の逆元が入っている

def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs

def modnCr(n,r,mod,fac,inv): #上で求めたfacとinvsを引数に入れるべし(上の関数で与えたnが計算できる最大のnになる)
    return fac[n] * inv[n-r] * inv[r] % mod

def bitadd(a,w,bit): #aにwを加える(1-origin)
 
    x = a
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-1 * x)
 
def bitsum(a,bit): #ind 1～aまでの和を求める
 
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret

import sys
from sys import stdin
N = int(stdin.readline())
a = list(map(int,stdin.readline().split()))

BIT = [0] * (N+1)

fac,inv = modfac(N+10,mod)
zeronum = 0
 
ans1 = 0
RZ = [0] * N
app = [False] * (N+1)
app[0] = True

for i in range(N-1,-1,-1):

    if a[i] != 0:
        ans1 += fac[N-1-i] * ( bitsum(a[i],BIT) )
        ans1 %= mod
        bitadd(a[i],1,BIT)
        app[a[i]] = True
    else:
        zeronum += 1
    RZ[i] = zeronum

mEX = [0] * (N+1) #数字x以下の数がいくつあるか
for i in range(1,N+1):
    if app[i] == False:
        mEX[i] = mEX[i-1] + 1
    else:
        mEX[i] = mEX[i-1]

ans1 *= fac[zeronum]

ans2 = 0
ans3 = 0
tmpinv = inverse(zeronum,mod)
tmpsum = 0
for i in range(N):
    if a[i] != 0:
        ans2 += fac[zeronum] * mEX[a[i]] * RZ[i] * tmpinv * fac[N-1-i]
        ans2 += fac[zeronum] * (zeronum-mEX[a[i]]) * tmpinv * tmpsum
        ans2 %= mod
    else:
        ans3 += fac[N-1-i] * fac[zeronum] * (RZ[i]-1) * inverse(2,mod)
        tmpsum += fac[N-1-i]

print (ans1 , ans2 , ans3 , fac[zeronum],file=sys.stderr)
print ((ans1 + ans2 + ans3 + fac[zeronum]) % mod)

