
def f(x):
    ret = 0
    while(x > 0):
        ret = ret + x % 10
        x = x // 10
    return ret

a,n,m = [int(i) for i in input().split()]

ans = 0
i = 1
ii = 1
while(ii <= m):
    if ii == (f(ii)+a)**n:
        ans += 1
    i += 1
    ii = i**n
#    print(i, ii)

print(ans)

