import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, b, k = M()
for i in range(k):
    if i % 2 == 0:
        # 高橋くんの場合
        if a % 2 == 1:
            a -= 1
        b = b + a//2
        a = a//2
    else:
        if b % 2 == 1:
            b -= 1
        a = a + b//2
        b = b//2
print(a, b)