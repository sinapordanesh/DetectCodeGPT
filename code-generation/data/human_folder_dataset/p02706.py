def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


n,m=sep()
ar=lis()
k=sum(ar)
if k>n:
    print(-1)
else:
    print(n-k)
