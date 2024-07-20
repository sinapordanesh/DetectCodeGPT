
"""
Writer: SPD_9X2
https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_d
左からおいていくことを考える
残ったカード全てから嫌われている場合、もう置くしかない
貪欲に置いていき、残りカード全てから嫌われてしまったら置く？

そうなるとただの実装難問題だが…

for i in range(N)
    if 残りのカード全てから嫌われてしまっているカードがあったら置く。
    elif 辞書順最小のカードが置けたら置く
    elif 辞書順2番目のカードが存在したら置く。
    else -1?

なのか？？
3枚以上なら絶対置くことが可能そうに見える


残りのカード全てから嫌われてしまっている、判定はどうすればよいと？
嫌われてる辞書(残存するカードのみ)を作っておき、len(辞書) == 2 で、1でない方が嫌われ者

elif 以降はheapqを使うのが良さそう
おいてるフラグ配列を管理しておき、置いてないが出るまでpop
置けない場合は、もう1つ出るまでpopし、置いて最初の奴を戻す

何が問題なんだ…？
この方法だとqueueが空になってしまうけど構成不可能ではない、ケースが存在する
N==2で-1は正しかった
互いに嫌いな2個が最後に残るとまずい
→最後の3つを全探索するか？
→これが丸そう
"""

def allserch(dnt,x,y,z):

    ret = []
    if dnt != x and a[x] != y and a[y] != z:
        ret.append([x,y,z])
    if dnt != x and a[x] != z and a[z] != y:
        ret.append([x,z,y])
    if dnt != y and a[y] != x and a[x] != z:
        ret.append([y,x,z])
    if dnt != y and a[y] != z and a[z] != x:
        ret.append([y,z,x])
    if dnt != z and a[z] != x and a[x] != y:
        ret.append([z,x,y])
    if dnt != z and a[z] != y and a[y] != x:
        ret.append([z,y,x])
    ret.sort()
    return ret[0]


import heapq
import sys

N = int(input())
a = list(map(int,input().split()))

if N == 2:
    print (-1)
    sys.exit()

for i in range(N):
    a[i] -= 1

ans = []
dont = None

hq = []
for i in range(N):
    heapq.heappush(hq,i)
    
usable = [True] * N
dic = {}
for i in range(N):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1


for loop in range(N-3):

    flag = True
    
    if len(dic) == 2:
        maxind = None

        for i in dic:
            if maxind == None:
                maxind = i
            elif dic[i] > dic[maxind]:
                maxind = i

        if dic[maxind] == (N-loop-1) and usable[maxind]:
            nc = maxind
            flag = False

    if flag:

        while (not usable[hq[0]]):
            heapq.heappop(hq)
            
        fi = heapq.heappop(hq)
        if dont != fi:
            nc = fi
        else:

            while (not usable[hq[0]]):
                heapq.heappop(hq)

            
            sec = heapq.heappop(hq)
            heapq.heappush(hq,fi)
            nc = sec

    #print (nc,a[nc])
    ans.append(nc+1)
    usable[nc] = False
    dic[a[nc]] -= 1
    dont = a[nc]
    if dic[a[nc]] == 0:
        del dic[a[nc]]

pas = []
while len(hq) > 0:
    now = heapq.heappop(hq)
    if usable[now]:
        pas.append(now)

rec = allserch(dont,pas[0],pas[1],pas[2])
for i in range(3):
    rec[i] += 1
ans += rec

print (*ans)     
  