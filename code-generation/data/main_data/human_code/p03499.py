n, = map(int, input().split())
p = [-1] + [*map(int, input().split())]

MOD = 10**9+7
dp = [[] for _ in range(n+1)]
dep = [0]*(n+1)
nxt = [0]*(n+1)

for v in range(n,0,-1):
    _,nxt[p[v]],dep[p[v]] = sorted([nxt[p[v]],dep[p[v]],dep[v]+1])

tot = [0]*(dep[0]+1)
for i in range(n+1): tot[dep[i]] += 1

def merge(p,v):
    if len(dp[p]) < len(dp[v]):
        dp[p],dp[v]=dp[v],dp[p]
    for i in range(-len(dp[v]),0):
        a,b,c = dp[p][i]
        d,e,f = dp[v][i]
        dp[p][i][:] = [a*d%MOD,(b*d+a*e)%MOD,c*f%MOD]

for v in range(n,-1,-1):
    dp[v].append([1,1,2])
    for i in range(-nxt[v]-1,0):
        dp[v][i][0] = dp[v][i][2] - dp[v][i][1]
    if v: merge(p[v],v)

ans = 0
for d in dp[0]:
    ans += pow(d[2],MOD-2,MOD)*d[1]%MOD
print(ans*pow(2,n+1,MOD)%MOD)