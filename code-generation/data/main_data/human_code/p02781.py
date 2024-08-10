import math
n=int(input())
k=int(input())

def comb(n,k):
    s=1
    for i in range(k):
        s*=n-i
    for i in range(k):
        s//=i+1
    return s

def ans(n,k):

    s=0
    if int(str(n)[0])==0:
        return 0
    if len(str(n))<k:
        return 0
    elif len(str(n))==k:
        s+=(int(str(n)[0])-1) * comb(len(str(n))-1,k-1)*9**(k-1)
        if k-1==0:
            s+= 1
        else:
            s+= ans(int(str(n)[1:]),k-1)
        return s
    else:
        s += (int(str(n)[0]) - 1) * comb(len(str(n)) - 1, k - 1) * 9 ** (k - 1)
        if k-1==0:
            s+= 1
        else:
            s+= ans(int(str(n)[1:]),k-1)
        s+=comb(len(str(n))-1,k)*9**(k)
        return s

print(ans(n,k))