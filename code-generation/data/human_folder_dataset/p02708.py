def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

N=10**9 + 7
n,K=sep()
s=0
for k in range(K,n+2):
    s= (s + (k*(n-k+1))%N + 1)%N
print(s)


