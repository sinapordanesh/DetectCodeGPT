import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=998244353
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()
  ans=set()
  if n%2==0:
    for i in range(n):
      for j in range(i+1,n):
        if i==j:
          continue
        if n+1==(i+1)+(j+1):
          continue
        ans.add((i+1,j+1))
  else:
    for i in range(n):
      for j in range(i+1,n):
        if i==j:
          continue
        if n==(i+1)+(j+1):
          continue
        ans.add((i+1,j+1))
  print(len(ans))
  for x,y in ans:
    print(x,y)

main()
# print(main())
