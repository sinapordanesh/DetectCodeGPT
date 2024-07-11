def resolve():
    n = int(input())
    a = tuple(map(int,input().split()))
    ans = 'APPROVED'
    for i in a:
        if i%2:continue
        if i%3!=0 and i%5!=0:
            ans = 'DENIED'
    print(ans)
resolve()