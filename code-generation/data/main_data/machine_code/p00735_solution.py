def monday_saturday_prime_factors():
    def factorize(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n**0.5)+1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    
    n = int(input())
    while n != 1:
        factors = factorize(n)
        print(str(n) + ":", end=" ")
        for factor in sorted(factors):
            print(factor, end=" ")
        print()
        n = int(input())