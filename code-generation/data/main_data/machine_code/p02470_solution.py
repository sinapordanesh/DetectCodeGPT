def euler_phi(n):
    phi = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            phi -= phi // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        phi -= phi // n
    return phi

n = int(input())
print(euler_phi(n))