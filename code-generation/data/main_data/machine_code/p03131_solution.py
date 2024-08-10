def max_biscuits(K, A, B):
    if A + 1 >= B:
        return K + 1
    elif K <= A:
        return K + 1
    else:
        return (K - A) // 2 * (B - A) + A + (K - A) % 2 + 1

# Test the function with the sample inputs
print(max_biscuits(4, 2, 6))
print(max_biscuits(7, 3, 4))
print(max_biscuits(314159265, 35897932, 384626433))