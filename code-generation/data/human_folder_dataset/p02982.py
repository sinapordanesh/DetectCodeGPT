import math
n,d = map(int,input().split(" "))
clist = []

for i in range(n):
    xlist = list(map(int,input().split(" ")))
    clist.append(xlist)

def dis(ylist,zlist):
    distance = 0
    for i in range(d):
        distance += (ylist[i] - zlist[i]) ** 2
    sqdis = math.sqrt(distance)
    return(sqdis)

countdis = 0

for i in range(n-1):
    for j in range(i+1,n):
        if dis(clist[i],clist[j]) % 1 == 0:
            countdis += 1

print(countdis)