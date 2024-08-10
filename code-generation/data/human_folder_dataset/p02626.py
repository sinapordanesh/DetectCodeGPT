def main(n,a):
    s=a[0]+a[1]
    z=0
    for ai in a[2:]:
        z^=ai
    # i+j=s,i<=a[0],i^j=z となるi,jを探す
    # i+j=i^j+2*(i & j)
    # s = z + 2*(i & j)
    # i & j = (s-z)/2 = d
    # z = 2*(i & j) - s = i ^ j
    # d = (s-z) / 2
    # z = x^y , x&y=0
    # d^x,d^yは条件を満たす。d^x+d^y=d^x^d^y + 2*((d^x)&(d^y))= z + 2*d = s
    # (d^x)^(d^y)=x^y=z
    # (d^x)&(d^y)=d (z & d = 0 のときのみ)
    if s-z<0 or (s-z)%2==1:return -1
    d=(s-z)//2
    if d&z!=0:return -1
    if not d<=a[0]:return -1
    part=[]
    i=0
    while z//pow(2,i):
        if (z//pow(2,i))%2==1:part.append(pow(2,i))
        i+=1
    ans=float('inf')
    k=len(part)
    x=0
    while part:
        tmp=part.pop()
        if d^(x+tmp)<=a[0]:
            x+=tmp
    return a[0]-(d^x) if d^x else -1


n=int(input())
a=list(map(int,input().split()))
print(main(n,a))