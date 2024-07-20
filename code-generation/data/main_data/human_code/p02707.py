def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


n=int(input())
ar=lis()
temp=[0]*(n+5)
for i in range(n-1):
    #print(ar[i],temp)
    temp[ar[i]]+=1
for i in range(1,n+1):
    print(temp[i])

