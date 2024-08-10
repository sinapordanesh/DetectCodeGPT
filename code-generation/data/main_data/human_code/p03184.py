MOD = 10**9+7

kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n): return kaijo_memo[n]
  if(len(kaijo_memo) == 0): kaijo_memo.append(1)
  while(len(kaijo_memo) <= n): kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n): return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0): gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n): gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if n == r: return 1
  if n < r or r < 0: return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

H,W,N = list(map(int,input().split()))
wall = [0,H*W-1]
for i in range(N):
  r,c = list(map(int,input().split()))
  wall.append((r-1)*W+(c-1))
  
wall.sort()

graph = [[] for i in range(N+2)]

for i in range(N+2):
  y,x = wall[i]//W, wall[i]%W
  for j in range(i+1,N+2):
    ny,nx = wall[j]//W, wall[j]%W
    if nx<x or ny<y: continue
    graph[j].append(i)

dp = [0 for i in range(N+2)]
for j in range(1,N+2):
  y,x = wall[j]//W, wall[j]%W
  dp[j] = nCr(y+x,y)
  for i in graph[j]:
    py,px = y-(wall[i]//W), x-(wall[i]%W)
    dp[j] -= nCr(py+px,py)*dp[i]
    dp[j] %= MOD

print(dp[-1])