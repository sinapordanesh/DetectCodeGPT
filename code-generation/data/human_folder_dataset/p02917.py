def resolve():
    n = int(input())
    b = list(map(int,input().split()))[::-1]
    ans = b[0]+b[-1]
    for i in range(n-2):
        ans += (min(b[i],b[i+1]))
    print(ans)
resolve()