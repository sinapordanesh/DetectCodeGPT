from math import gcd
def euler_phi(n):
    res=n
    for x in range(2,int(n**.5)+2):
        if n%x==0:
            res=(res//x)*(x-1)
            while n%x==0:
                n//=x
    if n!=1:
        res=(res//n)*(n-1)
    return res

def biggcd(n,m):
    g=gcd(n,m);res=g;count=2
    while gcd(g**count,m)>res:
        res=gcd(g**count,m)
        count+=1
    return res

def solve(a,m,n):
    if gcd(a,m)==1:
        if m==1: return 1
        phi=euler_phi(m);G=gcd(phi,m);r0=solve(a,G,n);mod=m*phi//G
        return ((((pow(a,n*r0,mod)-n*r0)%mod)//G)*pow(n*phi//G,phi-1,m)*phi+r0)%mod
    big=biggcd(a,m);k0=solve(a,m//big,n*big)
    return big*k0

for i in range(int(input())):
    A,M=map(int,input().split())
    print(solve(A,M,1))
