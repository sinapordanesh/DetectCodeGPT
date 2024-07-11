def resolve():
    k,x = map(int,input().split())
    print(' '.join(str(i) for i in range(x-k+1,x+k)))
resolve()