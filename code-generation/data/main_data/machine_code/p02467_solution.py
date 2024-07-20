def prime_factorization(n):
    print(n, end=': ')
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i, end=' ')
    if n > 1:
        print(n, end=' ')

n = int(input())
prime_factorization(n)