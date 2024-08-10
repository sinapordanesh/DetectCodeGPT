# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline
sys.setrecursionlimit(10**5)

k,n = map(int, read().split())

if k%2==0:
    print(*([k//2]+[k]*(n-1)))
    exit()

if k==1:
    print(*[1]*((n+1)//2))
    exit()

ans = [(k+1)//2]*n
d = 0
def f(k,i,d):
    # d <= 1+k+...+k^i?
    v = 1
    for j in range(i):
        v *= k
        v += 1
        if v > d: return True
    return False

def g(k,i):
    # 1+k+...+k^i
    v = 1
    for j in range(i):
        v *= k
        v += 1
    return v
    
for i in range(1,n):
    if f(k,n-i-1,d):
        d += 1
        continue
    """
    以下　300000 >= d >= 1+k+...+k^(n-i-1)
    i 番目の項から真ん中にならない    
    v 番目を目指す
    """
    v = (g(k,n-i)+d+1)//2 - d - 1
    
    for j in range(i,n):
        #print(v)
        if v==0:
            ans[j] = 0
            continue

        p = g(k,n-j-1)
        q = (v-1)//p 
        #print(v,j,p,q)
        
        ans[j] = q+1
        v -= 1+q*p        



    
    break


while ans[-1]==0:
    ans.pop()
print(*ans)







