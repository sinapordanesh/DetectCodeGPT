def num_divisors(n):
    mod = 10**9 + 7
    factorial = 1
    for i in range(1, n+1):
        factorial = (factorial * i) % mod
    
    divisors = 1
    i = 2
    while i*i <= factorial:
        count = 0
        while factorial % i == 0:
            count += 1
            factorial //= i
        divisors = (divisors * (count+1)) % mod
        i += 1
    
    if factorial > 1:
        divisors = (divisors * 2) % mod
    
    return divisors

# Read input from stdin
n = int(input())
print(num_divisors(n))