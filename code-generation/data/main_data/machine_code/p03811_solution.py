def swap_coprime_integers(N, A):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def is_coprime(a, b):
        return gcd(a, b) == 1

    for i in range(N):
        for j in range(i+1, N):
            if A[j] < A[i] and is_coprime(A[i], A[j]):
                A[i], A[j] = A[j], A[i]

    return A

# Sample Input 1
N = 5
A = [1, 2, 3, 4, 5]
print(*swap_coprime_integers(N, A))

# Sample Input 2
N = 4
A = [2, 3, 4, 6]
print(*swap_coprime_integers(N, A))