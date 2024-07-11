def dfs(i,r,g,b):
    global ans
    if i == k:
        if r < g and g < b:
            ans += 1
        return
    dfs(i+1,r*2,g,b)
    dfs(i+1,r,g*2,b)
    dfs(i+1,r,g,b*2)

a,b,c = map(int,input().split())
k = int(input())
ans = 0
dfs(0,a,b,c)
if ans > 0:
    print('Yes')
else:
    print('No')