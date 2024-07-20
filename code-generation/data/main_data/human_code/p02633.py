m = int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
x = make_divisors(360)

#最大公約数
def gcd(a,b):
    if(b>a):
        a,b=b,a
    i=b
    while i>0:
        if(a%i==0 and b%i==0):
            return i
        i-=1

#最小公倍数
def lcm(a,b):
    return int(a*b/gcd(a,b))

y = lcm(m,360)

if m in x:
    print(360//m)
else:
    print(y//m)