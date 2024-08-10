
def ans_is_zero():
    print(0)
    exit(0)

def solve():
    n=int(input())
    if n > 23: ans_is_zero()

    d=list(map(int,input().split()))
    for num in d:
        if num == 0: ans_is_zero()

    ans=0
    d.sort()

    N = 1 << n
    for i in range(N):#left or right
        t=1
        ret = 100

        for j in range(n):
            if (i>>j)&1: num = d[j]
            else: num = 24 - d[j]

            if (t >> num)&1:
                ret = -1
                break
            t |= (1 << num)

        if ret == -1: continue
        prev = 0

        for j in range(1, 24):
            if ((t>>j)&1) == 0: continue
            ret = min(ret, j - prev)
            prev = j

        ret = min(ret, 24-prev)
        ans = max(ans, ret)
    print(ans)
solve()
