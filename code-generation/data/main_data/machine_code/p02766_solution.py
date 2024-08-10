def number_of_digits_in_base(N, K):
    return len(str(N)) if K == 10 else len((str(N) if N != 0 else '0')) + 1

# Sample Input 1
print(number_of_digits_in_base(11, 2)) # Sample Output 1: 4

# Sample Input 2
print(number_of_digits_in_base(1010101, 10)) # Sample Output 2: 7

# Sample Input 3
print(number_of_digits_in_base(314159265, 3)) # Sample Output 3: 18