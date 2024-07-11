def resolve():
    a,b = map(int,input().split())
    print(0 if a<b*2 else a-b*2)
resolve()