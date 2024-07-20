def max_gcd(N, A):
    from math import gcd
    max_value = max(A)
    count = 0
    for i in range(N):
        if A[i] == max_value:
            count += 1
    if count > 1:
        return max_value
    else:
        max_divisor = 1
        for i in range(1, int(max_value**0.5) + 1):
            if max_value % i == 0:
                max_divisor = max(max_divisor, i)
                max_divisor = max(max_divisor, max_value // i)
        return max_divisor

# Sample Input 1
print(max_gcd(3, [7, 6, 8]))

# Sample Input 2
print(max_gcd(3, [12, 15, 18]))

# Sample Input 3
print(max_gcd(2, [1000000000, 1000000000]))