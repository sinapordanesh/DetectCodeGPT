def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]
def MI(): return map(int, input().split())
#1:set
#1_A
"""
n,q = map(int, input().split(" "))
group = [[i] for i in range(n)]
key = [i for i in range(n)]
for i in range(q):
    com, x, y = map(int, input().split(" "))
    if com == 0:
        if key[x] != key[y]:
            v = key[y]
            group[key[x]] = group[key[x]] + group[key[y]]
            for j in group[v]:
                key[j] = key[x]
            group[v] = []
    if com == 1:
        if key[x] == key[y]:
            print(1)
        else:
            print(0)
"""
#1_B
"""
def root(x,n):
    if par[x][0] == x:
        return [x,n+par[x][1]]
    return root(par[x][0],par[x][1])
def unite(x,y):
    rx = root(x)
    ry = root(y)
    if rx[0] == ry[0]:
        return
    par[rx][0] = ry[0]
    par[rx][1] += ry[1]
n,q = map(int, input().split(" "))
par = [[i,0] for i in range(n)]
for i in range(q):
    q = list(map(int, input().split(" ")))
    if q[0] == 0:

        if root(q[1],0) != root(q[])
"""
#2:range quary
#2_A
"""
n,q = map(int, input().split(" "))
k = 2**31-1
a = [float("inf") for i in range(n)]
for i in range(q):
    com, x, y = map(int, input().split(" "))
    if com == 0:
        a[x] = y
    else:
        mi = k
        for j in range(x, y+1):
            if a[j] == float("inf"):
                mi = min(mi, k)
            else:
                mi = min(mi,a[j])
        print(mi)
"""
#2_B

#2_C

#2_D

#2_E

#2_F

#2_G

#2_H

#2_I


#3:sliding window
#3_A
n,s = MI()
a = LI()
for i in range(1,n):
    a[i] += a[i-1]
a.insert(0,0)
l = 0
r = 0
ans = float("inf")
if a[1] >= s:
    print(1)
    quit()
while r < n:
    r += 1
    if a[r]-a[l] >= s:
        while a[r]-a[l] >= s and l < r:
            l += 1
        ans = min(ans, r-l+1)
if ans == float("inf"):
    print(0)
    quit()
print(ans)
#4:coordinate compression


#5:comulative sum
#5_A
"""
n,t = map(int, input().split(" "))
num = [0 for i in range(t)]
for i in range(n):
    l,r = map(int, input().split(" "))
    num[l] += 1
    if r < t:
        num[r] -= 1
for i in range(1,t):
    num[i] += num[i-1]
print(max(num))
"""

#5_B
"""
n = int(input())
lec = [[0 for i in range(1001)] for j in range(1001)]
max_x = 0
max_y = 0
for i in range(n):
    x,y,s,t = map(int, input().split(" "))
    lec[y][x] += 1
    lec[y][s] -= 1
    lec[t][x] -= 1
    lec[t][s] += 1
    max_x = max(max_x, s)
    max_y = max(max_y, t)

for i in range(max_y+1):
    for j in range(1, max_x+1):
        lec[i][j] += lec[i][j-1]

for i in range(1, max_y+1):
    for j in range(max_x+1):
        lec[i][j] += lec[i-1][j]

ans = 0
for i in range(max_y+1):
    for j in range(max_x+1):
        ans = max(ans, lec[i][j])

print(ans)
"""

