#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = inl()
b = [(a[i],i) for i in range(n)]
b.sort(reverse=True)
b.append((0,0))
ans = [0]*n
v = b[0][1]
for i in range(n):
    ans[v] += (i+1)*(b[i][0]-b[i+1][0])
    v = min(v,b[i+1][1])
for i in range(n):
    print(ans[i])
