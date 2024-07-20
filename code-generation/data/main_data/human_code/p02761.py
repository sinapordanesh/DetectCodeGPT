def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n,m=sep()
def f():
    return -1
ar=[]
for _ in range(m):
    ar.append(tuple(sep()))
t=0

def istrue(n):
    s=str(n)
    for i in ar:
        if i[0]>len(s):
            return 0
        if s[i[0]-1]!=str(i[1]):
            return 0
    return 1


if n==1:
    for i in range(0, 10):
        if istrue(i):
            print(i)
            quit()
    print(-1)
    quit()



for i in range(10**(n-1),10**n):
    if istrue(i):
        print(i)
        quit()
print(-1)


