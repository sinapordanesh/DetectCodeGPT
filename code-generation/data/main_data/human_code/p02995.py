A,B,C,D = map(int,input().split())

def gcd(x,y):
    if(x == 0):
        return y
    if(y == 0):
        return x
    if(x >= y):
        return gcd(y,x%y)
    if(x < y):
        return gcd(y%x,x)

l = (C * D) // gcd(C,D)

p = B//C - (A-1)//C
q = B//D - (A-1)//D
r = B//l - (A-1)//l
s = p + q - r
print(B-A+1-s)