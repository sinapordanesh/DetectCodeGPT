def getval():
    n = int(input())
    a = list(map(int,input().split()))
    return n,a

def main(n,a):
    m = 1000
    f = 0
    for i in range(n):
        if i>0:
            if a[i]>a[i-1]:
                m += f*a[i]
                f = 0
        if i<n-1:
            if a[i]<a[i+1]:
                f += m//a[i]
                m %= a[i]
    if f!=0:
        m += f*a[i-1]
    print(m)
            

if __name__=="__main__":
    n,a = getval()
    main(n,a)