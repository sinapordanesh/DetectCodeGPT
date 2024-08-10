n,x=map(int,input().split())
def f(a,b):
    if a>b: b,a=a,b 
    if b%a==0: return (2*(b//a)-1)*a
    return 2*a*(b//a)+ f(b%a,a)
print(n+ f(x,n-x))
