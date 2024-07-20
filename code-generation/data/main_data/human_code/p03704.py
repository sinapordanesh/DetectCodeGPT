
"""

https://atcoder.jp/contests/arc075/tasks/arc075_d

桁数を決め打ちする？
 abcd
-dcba
 ABCD

999a+90b-90c-999d = ABCD

みたいな感じになる
これをいい感じに満たせばおk
aとd,bとcをまとめる
-9～9の19通り


19**4 = 2476099通り
aとdの分配の仕方の通り数をあらかじめ数えておけばおｋ
ただし、a != 0
差は、9999109999
      9999019999
差があるとDを超える場合は探索を打ち切ればおｋ

"""
import sys

def dfs(dig,nd,nsum):

    P = 10**((dig-1)-nd) - 10**nd #この桁の寄与の基準
    maxc = 10**((dig-1)-nd)
    
    if nd == dig//2:
        if nsum == D:
            if dig % 2 == 0:
                return 1
            else:
                return 10
        return 0
    elif nd != 0:
        ret = 0
        for i in range(-9,10):
            if nsum+P*i < D-maxc or nsum+P*i > D+maxc:
                continue
            ret += dfs(dig,nd+1,nsum+P*i) * sums[i]
        #print (ret,"y")
        return ret
    else:
        ret = 0
        for i in range(-9,10):
            if nsum+P*i < D-maxc or nsum+P*i > D+maxc:
                continue
            tmp = dfs(dig,nd+1,nsum+P*i) * sums_z[i]
            #if tmp > 0:
            #    print (dig,nd+1,i,"is 1",tmp)
            ret += tmp
        return ret
            

D = int(input())
ans = 0
sums = [0] * 30
for i in range(-9,10):
    for x in range(-9,1):
        for y in range(0,10):
            if x+y == i:
                sums[i] += 1
print (sums , file=sys.stderr)
sums_z = [0] * 30
for i in range(-9,10):
    for x in range(-9,0):
        for y in range(1,10):
            if x+y == i:
                sums_z[i] += 1
print (sums_z , file=sys.stderr)

for dig in range(1,20):

    now = dfs(dig,0,0)
    #print (dig,now)
    ans += now

print (ans)
