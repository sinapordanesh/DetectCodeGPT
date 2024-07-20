def f(n,a):
    if n==1:
        print(1)
        exit()
    pre=a[1]-a[0]
    ans=1
    for i in range(2,n):
        if pre*(a[i]-a[i-1])<0:
            pre=0
            ans+=1
        else:
            if a[i]-a[i-1]:###
                pre=a[i]-a[i-1]
    return ans

n=int(input())
*a,=map(int,input().split())
print(f(n,a))