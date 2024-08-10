def find_sets_of_ramen(N, M):
    def power(x, y, m):
        if y == 0:
            return 1
        p = power(x, y // 2, m)
        p = p * p % m
        if y % 2 == 0:
            return p
        else:
            return p * x % m
    
    result = power(2, N, M) - 1
    for i in range(1, N):
        result = (result - (power(2, math.gcd(i, N), M) - 1)) % M
        
    return result

N, M = map(int, input().split())
print(find_sets_of_ramen(N, M))