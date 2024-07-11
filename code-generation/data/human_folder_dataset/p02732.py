def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
from collections import Counter
ar=lis()
c=Counter(ar)
s=0
for i in c.values():
    s+=((i*(i-1))//2)
for i in ar:
    print(s-c[i]+1)
