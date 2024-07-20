import sys
input = sys.stdin.readline
from collections import deque

h,w = map(int,input().split())
s = []
for i in range(h):
  q = input().rstrip()
  s.append(q)

chk = [[0]*(w-1) for i in range(h-1)]
for i in range(w-1):
  for j in range(h-1):
    chk[j][i] = 1-int((s[j][i]=='#')^(s[j+1][i]=='#')^(s[j][i+1]=='#')^(s[j+1][i+1]=='#'))

def f(a):
  a += [0]
  stack = deque()
  ans = -1
  for i in range(w):
    if stack == deque():
        stack.append((a[i], i))
    elif stack[-1][0] < a[i]:
        stack.append((a[i], i))
    elif stack[-1][0] > a[i]:
      while stack and stack[-1][0] >= a[i]:
        x, y = stack.pop()
        ans = max((x+1)*(i-y+1), ans)
      stack.append((a[i], y))
  return ans
  
dp = [[0]*(w-1) for i in range(h-1)]
for i in range(w-1):
  dp[0][i] = chk[0][i]
  
for i in range(1,h-1):
  for j in range(w-1):
    if chk[i][j]:
      dp[i][j] = dp[i-1][j]+1

ans=max(h,w)
for i in range(h-1):
    ans=max(ans,f(dp[i]))
    
print(ans)