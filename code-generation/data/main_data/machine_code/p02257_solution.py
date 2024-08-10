def count_prime_numbers():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
    
    print(count)

count_prime_numbers()