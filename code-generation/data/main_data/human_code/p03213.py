from collections import Counter
from math import factorial

def prime_factorize(n):
    a = []
    while n%2 == 0:
        a.append(2)
        n //=2
    f = 3
    while f*f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def prime_factoring(n):
    from collections import Counter
    a = prime_factorize(n)
    return Counter(a)

N = int(input())
fac =factorial(N)
List = prime_factoring(fac).values()
# print(List)

def num(m):
    return len(list(filter(lambda x: x >= m-1, List)))
print(num(75)+ num(25)*(num(3)-1) + num(15)*(num(5)-1)+ num(5)*(num(5)-1)*(num(3)- 2)//2)
