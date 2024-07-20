def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

s=input()
q=int(input())
from collections import deque
ar=[]
for i in s:
    ar.append(i)
ar=deque(ar)
r=0
for i in range(q):
    t=[i for i in input().strip().split(" ")]
    if t[0]=="1":
        r=1-r
    else:
        if r==0:
            if t[1]=="1":
                ar.appendleft(t[2])
            else:
                ar.append(t[2])
        else:
            if t[1]=="1":
                ar.append(t[2])
            else:
                ar.appendleft(t[2])
if r==0:
    print("".join(ar))
else:
    print("".join(ar)[::-1])
