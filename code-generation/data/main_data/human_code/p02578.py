def A():
    n, x, t = map(int, input().split())
    print(t * ((n+x-1)//x))

def B():
    n = list(input())
    s = 0
    for e in n:
        s += int(e)
    print("Yes" if s % 9 == 0 else "No")

def C():
    int(input())
    a = list(map(int, input().split()))
    l = 0
    ans = 0
    for e in a:
        if e < l: ans += l - e
        l = max(l, e)
    print(ans)

C()
