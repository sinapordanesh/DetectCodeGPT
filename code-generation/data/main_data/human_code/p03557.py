def II(): return int(input())
def LII(): return list(map(int, input().split()))

n=II()
alist=LII()
blist=LII()
clist=LII()

alist.sort()
blist.sort()
clist.sort()

#あるbより小さいaの数
def count_a(b):
    ok,ng = -1,n
    def is_ok(i):
        return alist[i]<b
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok+1

def count_c(b):
    ok,ng = n,-1
    def is_ok(i):
        return clist[i]>b
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return n-ok

result=0
for b in blist:
    result += count_a(b) * count_c(b)

print(result)