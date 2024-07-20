def arithmetic_progression(L, A, B, M):
    terms = [str(A + B * i) for i in range(L)]
    concatenated = int(''.join(terms))
    return concatenated % M

# Sample Input 1
print(arithmetic_progression(5, 3, 4, 10007))

# Sample Input 2
print(arithmetic_progression(4, 8, 1, 1000000))

# Sample Input 3
print(arithmetic_progression(107, 10000000000007, 1000000000000007, 998244353))