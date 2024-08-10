n, m = map(int, input().split())
a = sorted([int(x) for x in input().split()])


def chk(x):
    for i in range(2*x, 2*n):
        if i != 2*n - 1 - (i - 2*x) and a[i] + a[2*n-1-(i-2*x)] < m:
            return False
    return True


bottom = -1
top = n

while top - bottom > 1:
    mid = (top + bottom)//2
    if chk(mid):
        top = mid
    else:
        bottom = mid

ans = -1

for i in range(2*top, 2*n):
    ans = max(ans, (a[i]+a[2*n-1-(i-2*top)]) % m)
for i in range(2*top):
    ans = max(ans, (a[i] + a[2*top-1-i]) % m)

print(ans)
