import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque, defaultdict
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations,product#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
from functools import reduce,lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printe(*x):print("## ",*x,file=sys.stderr)
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]
def binr(x): return bin(x)[2:]
def bitcount(x): #xは64bit整数
    x= x - ((x >> 1) & 0x5555555555555555)
    x= (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x= (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f 
    x+= (x >> 8); x+= (x >> 16); x+= (x >> 32) 
    return x & 0x7f

def main():
    #C - Interval Game
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    base=N
    ls=[];rs=[]
    for i,(l,r) in enumerate(S):
        heappush(ls,-l*base+i)
        heappush(rs,r*base+i)
    
    dset=set()
    cur=0
    tot=0
    f=0
    lsc=ls.copy()
    rsc=rs.copy()
    while ls and rs:
        while ls:
            l,i=divmod(heappop(ls),base)
            l*=-1
            if i in dset:
                dset.remove(i)
            elif cur<l:
                tot+=l-cur
                dset.add(i)
                cur=l
                break
            else:
                f=1
                break
        if f:
            break
        while rs:
            r,i=divmod(heappop(rs),base)
            if i in dset:
                dset.remove(i)
            elif cur>r:
                tot+=cur-r
                cur=r
                dset.add(i)
                break
            else:
                f=1
                break
        if f:
            break
    tot+=abs(cur)

    ls=lsc
    rs=rsc
    dset=set()
    cur=0
    tot2=0
    f=0
    while ls and rs:
        while rs:
            r,i=divmod(heappop(rs),base)
            if i in dset:
                dset.remove(i)
            elif cur>r:
                tot2+=cur-r
                cur=r
                dset.add(i)
                break
            else:
                f=1
                break

        if f:
            break
        while ls:
            l,i=divmod(heappop(ls),base)
            l*=-1
            if i in dset:
                dset.remove(i)
            elif cur<l:
                tot2+=l-cur
                dset.add(i)
                cur=l
                break
            else:
                f=1
                break
            if f:
                break
    tot2+=abs(cur)

    print(max(tot,tot2))




if __name__ == "__main__":
    main()