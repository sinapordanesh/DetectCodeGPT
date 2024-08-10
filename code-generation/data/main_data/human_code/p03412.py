import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = 29
val = 0

def lcount(a,b,x):
    """ソート済a,bに対して, a[i]+b[j]<=xなるi,jの個数
    """
    la = len(a)
    lb = len(b)
    j = -1
    ans = 0
    for i in range(la-1, -1, -1):
        while j+1<lb and a[i]+b[j+1]<=x:
            j += 1
        ans += (j+1)
    return ans
for k in range(l):
    # i桁目を求める
    tmp = pow(2, k+1)
    bb = [item%(tmp) for item in b]
    aa = [item%(tmp) for item in a]
    aa.sort()
    bb.sort()
    ans = n**2 - lcount(aa,bb,tmp//2*3-1) + lcount(aa,bb,tmp-1) - lcount(aa,bb,tmp//2-1)
    if ans%2:
        val += pow(2, k)
print(val)