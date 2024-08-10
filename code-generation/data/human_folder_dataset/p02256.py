
c,d = list(map(int,input().split()))

if d>c:
    a = d
    b = c
else:
     a = c
     b = d

def gcd(x,y):
    if y == 0:
        return x
    else:
        r = x%y
        return gcd(y,r)
    
print(gcd(a,b))
    

