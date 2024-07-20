
"""

https://atcoder.jp/contests/agc035/tasks/agc035_d

毎回1枚カードが減り、寄与が2倍になる
両端のカードは消せない → 寄与は1倍のまま

端から2枚目のカードしか選ばなくていいみたいなの無いかな？
端から2枚目を選ぶと、1つは端の寄与になり、もう一つは動の寄与になる
つまり、動の寄与の総和は変化しない
そうでないのを選ぶと、動の寄与に2倍かかる

→ 2**18 になっていい感じのオーダーにはなる

検証：
5枚で真ん中を最初に選ぶべきなのを作れるか？
0,X,Y,Z,0
0,X+Y,Y+Z,0
0,X+2Y+Z,Y+Z
X+2Y+Z,X+3Y+2Z
→2X+3Y+3Z or 3X+3Y+2Z (真ん中を選んだ場合)

0,X,Y,Z,0
X,X+Y,Z,0 → X,X+Y+Z,Z → 2X+Y+Z,X+Y+2Z → 3X+2Y+3Z
2X+Y,X+Y+Z,0 → 3X+2Y+Z,X+Y+Z → 4X+3Y+2Z

すなわち、真ん中を選んだ方がいい場合もある…
最後まで残した数は2倍だけの寄与で済む
最後まで残す数を決め打ちする？
最後の数で左右を分ける
→さらにその区間で最後に残すやつは3倍の寄与で済む

1 4 3 5 2 5 3 4 1
→こんな感じ

あとは分割統治で、
ある点で区切った場合の左右の最小を足して上に返せばよい
計算量は？
長さ1の場合1
2の場合 1+1 = 2
3の場合 2+1+1+2 = 6
4の場合 6+

dp[0] = 0
dp[1] = 1
dp[n] = 2*(dp[n-1]+dp[n-2]…+dp[0])
dp[16] = 9565938 なので十分可能

"""

from sys import stdin

def want(l,r,lb,rb):
    if l > r:
        return 0
    elif l == r:
        return A[l] * (lb+rb)
    
    nmin = float("inf")
    for i in range(l,r+1):
        nmin = min(nmin , A[i]*(lb+rb) + want(l,i-1,lb,lb+rb) + want(i+1,r,lb+rb,rb) )
    return nmin
    

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

print (A[0] + A[-1] + want(1,N-2,1,1) )
