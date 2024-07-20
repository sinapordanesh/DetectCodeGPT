import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#https://atcoder.jp/contests/cf17-final-open/tasks/cf17_final_a
s=list(ss())
if len(list(s))>9:
    print("NO")
    exit()

ans =[]

kih=["K","I","H"]
b=["B"]
r=["R"]

chk=False
for i in list(product([0,1], repeat=4)):
    a1,a2,a3,a4=[],[],[],[]
    if i[0]==1:
        a1.append("A")
    if i[1]==1:
        a2.append("A")
    if i[2]==1:
        a3.append("A")
    if i[3]==1:
        a4.append("A")
    
    if s==a1+kih+a2+b+a3+r+a4:
        chk=True
    #print(a1+kih+a2+b+a3+r+a4)
if chk==True:
    print("YES")
else:
    print("NO")
