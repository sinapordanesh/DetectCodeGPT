def largest_integer(N, M, A):
    matchsticks = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    A.sort(reverse=True)
    result = ""

    while N > 0:
        for digit in A:
            while matchsticks[digit-1] <= N:
                result += str(digit)
                N -= matchsticks[digit-1]

    return int(result) if result else 0

# Sample Input 1
print(largest_integer(20, 4, [3, 7, 8, 4]))

# Sample Input 2
print(largest_integer(101, 9, [9, 8, 7, 6, 5, 4, 3, 2, 1]))

# Sample Input 3
print(largest_integer(15, 3, [5, 4, 6]))