def kth_largest_divisor(A, B, K):
    divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    
    return divisors[-K]