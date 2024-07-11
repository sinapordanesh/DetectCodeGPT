import itertools
def resolve():
    n = int(input())
    d = tuple(map(int,input().split()))
    ans = 0
    for a in itertools.combinations(d,2):
        ans += a[0]*a[1]
    print(ans)
resolve()