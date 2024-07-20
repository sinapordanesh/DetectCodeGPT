def solve():
    n, k = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    
    if sum(b) == n: 
        print(-1)
    else:
        res = 0
        for i in range(n):
            if b[i] == 1:
                res += a[i]
        print(res * 2)
        
solve()