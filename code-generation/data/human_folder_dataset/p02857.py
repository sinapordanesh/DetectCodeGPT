import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
# 標準出力による質問 interactive

import sys
count = 0
def query(l):
    global count
    count = count + 1
    if count>210:
        assert False
    print("? %s" % " ".join(map(str, l)))
    sys.stdout.flush()
    return input()

color = query(list(range(1,n+1)))
l = 1
r = n+1
while l<r-1:
    m = (l+r)//2
#     print("hoge")
    if color==query(range(m,m+n)):
        l = m
    else:
        r = m
ans = [None]*(2*n)
# r, ..., r+n-2に同数個
ll = list(range(r, r+n-1))
for i in range(1,2*n+1):
    if r<=i<=r+n-2:
        continue
    color = query(ll + [i])
    ans[i-1] = "B" if color=="Blue" else "R"
ll2 = []
bc = 0
rc = 0
for i in range(1,2*n+1):
    if r<=i<=r+n-2:
        continue
    if ans[i-1]=="R" and rc<n//2:
        rc += 1
        ll2.append(i)
    elif ans[i-1]=="B" and bc<n//2:
        bc += 1
        ll2.append(i)
assert len(ll2)==n-1
for i in range(r,r+n-1):
    color = query(ll2 + [i])
    ans[i-1] = "B" if color=="Blue" else "R"
# n==1のときは?
print("! %s" % "".join(map(str, ans)))