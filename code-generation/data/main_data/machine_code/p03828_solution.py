def positive_divisors_of_factorial(N):
    MOD = 10**9 + 7
    factorial = 1
    for i in range(1, N+1):
        factorial = (factorial * i) % MOD
    
    divisors = 1
    for i in range(1, factorial+1):
        if factorial % i == 0:
            divisors = (divisors * i) % MOD
    
    return divisors

N = int(input())
print(positive_divisors_of_factorial(N))