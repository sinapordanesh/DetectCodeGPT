t = int(input())
for _ in range(t):
    n,a,b,c,d = map(int,input().split())

    memo = {}
    def dfs(n):
        if n == 0:
            return 0
        if n == 1:
            return d
        if n in memo:
            return memo[n]
        res = min(
            d*n,
            d*((n+1)//2*2-n)+a+dfs((n+1)//2),
            d*(n-n//2*2)+a+dfs(n//2),
            d*((n+2)//3*3-n)+b+dfs((n+2)//3),
            d*(n-n//3*3)+b+dfs(n//3),
            d*((n+4)//5*5-n)+c+dfs((n+4)//5),
            d*(n-n//5*5)+c+dfs(n//5),
        )
        memo[n] = res
        return res

    print(dfs(n))
