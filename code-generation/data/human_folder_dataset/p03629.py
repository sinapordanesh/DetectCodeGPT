import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a = input()
n = len(a)
s = set()
l = []
i = n-1
prv = n
for c in a[::-1]:
    s.add(c)
    if len(s)==26:
        s = set()
        l.append((i,prv))
        prv = i
    i -= 1
def sub(i,j):
    """[i,j)に含まれない文字のうちの最小
    """
#     print(i,j)
    al = set([chr(v) for v in range(ord("a"), ord("z")+1)])
    for ind in range(i,j):
        al.discard(a[ind])
    return min(al)
ans = []
c = sub(0,prv)
ans.append(c)
while l:
    i,j = l.pop()
    for ind in range(i,n):
        if a[ind]==c:
            break
    c = sub(ind+1,j)
    ans.append(c)
ans = "".join(ans)
# else:
#     ans = "a" * (len(l)+1)
print(ans)