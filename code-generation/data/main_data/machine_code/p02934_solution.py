def find_multiplicative_inverse(N, A):
    total_inverse = sum([1/x for x in A])
    result = 1/total_inverse
    return result

# Sample Input 1
# N = 2
# A = [10, 30]
# Sample Output 1
# Expected Output: 7.5
print(find_multiplicative_inverse(2, [10, 30]))

# Sample Input 2
# N = 3
# A = [200, 200, 200]
# Sample Output 2
# Expected Output: 66.66666666666667
print(find_multiplicative_inverse(3, [200, 200, 200]))

# Sample Input 3
# N = 1
# A = [1000]
# Sample Output 3
# Expected Output: 1000
print(find_multiplicative_inverse(1, [1000]))