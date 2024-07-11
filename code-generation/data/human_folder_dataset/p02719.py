def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

n,k=sep()
if n>=k:
    n=(n%k)
print(min(n,abs(k-n)))
