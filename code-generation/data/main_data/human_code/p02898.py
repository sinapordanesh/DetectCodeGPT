import bisect
def resolve():
    n,k = map(int,input().split())
    h = sorted(list(map(int,input().split())))
    print(n-bisect.bisect_left(h,k))
resolve()