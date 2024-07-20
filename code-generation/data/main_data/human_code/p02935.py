def resolve():
    n = int(input())
    v = list(map(int,input().split()))
    v.sort(reverse=True)
    for _ in range(n-1):
        v = v[:-2]+ [(v[-1]+v[-2])/2]
    print(v[0])
resolve()