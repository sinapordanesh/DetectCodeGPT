def resolve():
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))
    before_dinner = a[0]
    ans = sum(b)
    for i in range(1,n):
        if a[i] - before_dinner==1:
            ans += c[before_dinner-1]
        before_dinner = a[i]
    print(ans)
resolve()