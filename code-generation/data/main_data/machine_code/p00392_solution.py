def common_prime_sort(N, arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def has_common_prime_factor(x, y):
        if gcd(x, y) != 1:
            return True
        return False
    
    for i in range(N-1):
        if not has_common_prime_factor(arr[i], arr[i+1]):
            return 0
    return 1