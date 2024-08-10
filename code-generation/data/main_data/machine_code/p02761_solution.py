def find_smallest_integer(N, M, digits):
    for num in range(10**(N-1), 10**N):
        num_str = str(num)
        if all(num_str[s-1] == str(c) for s, c in digits):
            return num
    return -1

# Sample Input 1
N = 3
M = 3
digits = [(1, 7), (3, 2), (1, 7)]
print(find_smallest_integer(N, M, digits))

# Sample Input 2
N = 3
M = 2
digits = [(2, 1), (2, 3)]
print(find_smallest_integer(N, M, digits))

# Sample Input 3
N = 3
M = 1
digits = [(1, 0)]
print(find_smallest_integer(N, M, digits))