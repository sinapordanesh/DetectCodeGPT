def resolve():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    print(a-(s==u),b-(t==u))
resolve()