def differ_by_1bit(n,end):
    if n==1:
        return [0,1]
    list=differ_by_1bit(n-1,0)
    for i in range(len(list)):
        q=list[i]//2**end
        r=list[i]%2**end
        list[i]=q*2**(end+1)+r
    list2=[2**end+list[-i-1] for i in range(len(list))]
    return list+list2

def differ_by_1bit_all(n):
    if n==1:
        return [0,1]
    if n%2==1:
        list1=differ_by_1bit_all(n-1)
        list2=differ_by_1bit(n-1,n-2)
        list2=[list2[i]^(2**(n-1)+2**(n-2)-1) for i in range(len(list2))]
        return list1+list2
    else:
        list1=differ_by_1bit(n-1,n-2)
        list1=[list1[i]<<1 for i in range(len(list1))]
        list2=differ_by_1bit_all(n-1)
        list2=[(list2[i]<<1)^(2**(n-1)+1) for i in range(len(list2))]
        return list1+list2

def convert(n,table):
    res=0
    for i in range(len(table)):
        if n>>i &1==1:
            res+=2**table[i]
    return res

def differ_by_1bit_free(n,end):
    T=[]
    F=[]
    for i in range(n):
        if end>>i &1==1:
            T.append(i)
        else:
            F.append(i)
    t=len(T)
    f=len(F)
    if t==n:
        return differ_by_1bit_all(n)
    list1=differ_by_1bit(f,0)
    list2=differ_by_1bit_all(t)
    res=[]
    for i in range(2**t):
        if i%2==0:
            res+=list1
        else:
            res+=list1[::-1]
    for i in range(2**n):
        res[i]=convert(res[i],F)
    for i in range(2**t):
        c=convert(list2[i],T)
        for j in range((2**f)*i,(2**f)*(i+1)):
            res[j]=res[j]^c
    return res

N,A,B=map(int,input().split())
test=B^A
check=0
for i in range(N):
    if test>>i &1==1:
        check+=1
if check%2==0:
    print("NO")
else:
    ans=differ_by_1bit_free(N,test)
    for i in range(len(ans)):
        ans[i]=ans[i]^A
    print("YES")
    print(*ans)