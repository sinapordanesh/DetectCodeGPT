def gcd(a,b):
    while b:a,b=b,a%b
    return a

def f(n,m):
    if m==1:return 0
    x=1
    for i in range(m):
        x=(x*n)%m
        if x==1:return i+1
        
while 1:
    a,b=map(int,input().split())
    if a==0:break
    c=gcd(a,b)
    a//=c;b//=c
    cnt=0;d=gcd(b,10)
    while d!=1:
        b//=d
        cnt+=1
        d=gcd(b,10)
    print(cnt,f(10,b))