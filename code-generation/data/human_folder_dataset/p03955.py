
"""

https://atcoder.jp/contests/agc006/tasks/agc006_e

まず、ちゃんと並んでない場合はだめ

3x+0
3x+1
3x+2
またはこれが上下反転されているもの以外が存在したら即NO
これを xと表すことにする。上下反転を-xと表すこととする
すると初期状態はxで表すと
1,2,3,4,5…,N　となる。

操作は、連続する3つを選び、両端を入れ替え、3つの項に-1を掛ける
となる。

そのため、偶奇が違う数があるとout
次に転倒数を考える。転倒数は交換するたびに1減る or 1増える
偶奇番目を分けて考える

交換すると、両端の偶奇の正負のパリティは変化しないが、反対側が変化する
よって、偶奇が逆の集合の転倒数を求める
→奇数ならば積は負・偶数なら積は正　が保たれる　そうでない場合はNO

それ以外はすべて作れるのか…？証明したい

 1 2 3 4
-3-2-1 4
-3-4 1 2

分からん…とりあえず出してみよう

"""

from sys import stdin
import sys

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

N = int(stdin.readline())

a = []
for i in range(3):
    tmp = list(map(int,stdin.readline().split()))
    a.append(tmp)

lis = []
bi  = []

for j in range(N):
    a[0][j] -= 1
    a[1][j] -= 1
    a[2][j] -= 1
    if a[0][j]//3 == a[1][j]//3 == a[2][j]//3 and a[0][j]//3%2 == j%2:
        if a[0][j] > a[1][j] > a[2][j]:
            lis.append(a[0][j]//3)
            bi.append(-1)
        elif a[0][j] < a[1][j] < a[2][j]:
            lis.append(a[0][j]//3)
            bi.append(1)
        else:
            print ("No")
            sys.exit()
    else:
        print ("No")
        sys.exit()

evenall = 1
for i in range(0,N,2):
    evenall *= bi[i]
oddall = 1
for i in range(1,N,2):
    oddall *= bi[i]


a = lis
#print (a,bi)
#even
BIT = [0] * (N+2)
ans = 0
for i in range(0,N,2):
    ans += i//2 - bitsum(a[i]+1,BIT)
    bitadd(a[i]+1,1,BIT)

#print (ans , oddall)
if (ans % 2 == 0 and oddall == -1) or (ans % 2 == 1 and oddall == 1):
    print ("No")
    sys.exit()

#odd
BIT = [0] * (N+2)
ans = 0
for i in range(1,N,2):
    ans += i//2 - bitsum(a[i]+1,BIT)
    bitadd(a[i]+1,1,BIT)

#print (ans , evenall)
if (ans % 2 == 0 and evenall == -1) or (ans % 2 == 1 and evenall == 1):
    print ("No")
    sys.exit()

print ("Yes")
