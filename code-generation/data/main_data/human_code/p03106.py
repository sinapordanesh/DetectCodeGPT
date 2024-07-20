A,B,K = map(int,input().split())

def cf(x1,x2):
    cf=[]
    for i in range(1,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

print(cf(A,B)[-(K)])