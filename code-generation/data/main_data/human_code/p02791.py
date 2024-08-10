def resolve():
    n = int(input())
    p = tuple(map(int,input().split()))
    min_p = p[0]
    cnt = 1
    for i in range(1,n):
        if min_p > p[i]:
            min_p = p[i]
            cnt += 1
    print(cnt)
resolve()