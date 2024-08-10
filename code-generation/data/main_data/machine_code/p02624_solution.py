def sum_of_divisors(N):
    def count_divisors(num):
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if num // i == i:
                    count += 1
                else:
                    count += 2
        return count
    
    result = 0
    for K in range(1, N+1):
        result += K * count_divisors(K)
    
    return result

N = int(input())
print(sum_of_divisors(N))