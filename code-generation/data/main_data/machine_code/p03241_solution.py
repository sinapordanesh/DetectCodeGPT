import math

def max_gcd(N, M):
    if M % N == 0:
        return M // N
    else:
        return math.gcd(M, M - N)
      
# Test the function
print(max_gcd(3, 14))
print(max_gcd(10, 123))
print(max_gcd(100000, 1000000000))