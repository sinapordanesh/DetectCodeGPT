def product_or_negative_one(N, A):
    result = 1
    for num in A:
        result *= num
        if result > 10**18:
            return -1
    return result

# Sample Input 1
print(product_or_negative_one(2, [1000000000, 1000000000]))

# Sample Input 2
print(product_or_negative_one(3, [101, 9901, 999999000001]))

# Sample Input 3
print(product_or_negative_one(31, [4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0]))