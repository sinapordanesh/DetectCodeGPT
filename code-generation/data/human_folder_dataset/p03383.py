"""

https://atcoder.jp/contests/arc095/tasks/arc095_c

列、行の文字の組み合わせは変わらない
→対応する列・行の組み合わせがなければだめ

→では、各組み合わせが2こずつちゃんとあれば必ず可能か…？
→だとしたら制約小さすぎない？？

ab
ba

abc
aba
cba

→多分十分条件ではないけど少なくとも各組み合わせが2こない場合は絶対×
→かつ、端数の文字が1こ以下でないとだめ
ダメな場合はなんだーーー

分からないけど探索すればよさそう
→ペアになる列・行さえ決まればいい

(11*9*7*5*3*1)**2　→ 10^8ぐらい　最大12**2回探索するので…ア
1ms解法は何…

あらかじめありうるペアだけ列挙しておく？
→あとの入れ替えは探索

→最大になるような場合は全部同じ場合なのですぐ答えが見つかる…と信じたい

1234
2341
3412
4123 →このパターンの場合最悪計算量になってしまう…

1234
2341
4123
3412

1243
2314
4132
3421→ok…？

必要十分条件なのか…？　700点だし…？

反例:
12Z34
23Y41
ZYXYZ
41Y23
34Z12


どうやら現実的な時間で解けるらしい
ちゃんと考えよう
→入れ替えた際に保持されるパラメータを考える…？

答えに対し、対称な列と行を入れ替えても問題ない
& 対称な列のset/行のsetを入れ替えても問題ない
→すなわち列・行の対応以外は全く関係ない

=====答えを見た=====
片側だけペアにするのか…
→確かに片側全探索したらもう片方は簡単に判定できる…(裏返しがあるか判定するだけなので)

具体的な実装は…
まずペアを列挙→再帰で適当にやる
→列を入れ替えたとする

次に横で見てって、各ペアの数字が全て対になってる物があるか調べればいい
→ペア通り数 * H * H * W
"""

def pair(end,lis):
    if len(lis) == 0:
        p.append(end)
        return
    else:
        end.append(lis[0])
        del lis[0]
        for j in range(len(lis)):
            pair( end+[lis[j]] , lis[:j]+lis[j+1:])

from sys import stdin
import sys

H,W = map(int,stdin.readline().split())

S = []
for i in range(H):
    s = stdin.readline()
    S.append(s[:-1])
#print (S)

#ペア列挙
p = []
if W % 2 == 0:
    pair([],[i for i in range(W)])
else:
    tmp = [i for i in range(W)]
    for i in range(W):
        pair([i,i] , tmp[:i] + tmp[i+1:])

#print (p)

for pl in p:
    able = [True] * H
    flag = 0

    for i in range(H):
        if able[i]:
            for j in range(i+1,H):
                if not able[j]:
                    continue

                tmpf = True
                for w in range((W+1)//2):
                    if S[i][pl[2*w]] != S[j][pl[2*w+1]] or S[j][pl[2*w]] != S[i][pl[2*w+1]]:
                        tmpf = False
                        break
                if tmpf:
                    able[i] = False
                    able[j] = False
                    break
            else:
                if H % 2 == 0 or flag == 1:
                    flag = 2
                    break
                for w in range((W+1)//2):
                    if S[i][pl[2*w]] != S[i][pl[2*w+1]]:
                        flag = 2
                        break
                else:
                    flag = 1
                    able[i] = False
                if flag == 2:
                    break
                
    if flag != 2:
        print ("YES")
        break
else:
    print ("NO")