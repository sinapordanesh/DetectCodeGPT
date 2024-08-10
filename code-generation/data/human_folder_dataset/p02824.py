n,m,v,p = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def solve(ind):
    if a[ind]+m < a[-p]:
        return False
    thr = a[ind] + m
    votes=[]
    for i in range(n):
        if i<=ind or i>n-p:
            votes.append(m)
        else:
            votes.append(thr-a[i])
    sm = sum(votes)
    return sm >= m*v

ok=n-1
ng=-1
while abs(ng - ok) > 1:
    mid = (ng + ok)//2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(n-ok)