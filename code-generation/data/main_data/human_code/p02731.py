def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=float(input())
k=n/3
print(k*k*k)