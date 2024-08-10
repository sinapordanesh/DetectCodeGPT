S = input()

ans = 0
def dfs(now, i):
    if i == len(S):
        global ans
        ans += eval(now)
        return
    dfs(now+"+"+S[i], i+1)
    dfs(now+S[i], i+1)
    
dfs(S[0],1)
print(ans)