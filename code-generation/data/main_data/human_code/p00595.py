def gcd(x, y):
    if y==0: return x
    z = x % y
    return gcd(y, z)
        
while True:
    try:
        a, b = (int(i) for i in input().split())
    except EOFError:
        break
    if a<b: print(gcd(b,a))
    else: print(gcd(a,b))
    