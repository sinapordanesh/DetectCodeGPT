def sum_of_integers(N, A, B):
    total = 0
    for i in range(1, N+1):
        if A <= sum(map(int, str(i))) <= B:
            total += i
    return total

# Sample Input 1
print(sum_of_integers(20, 2, 5))

# Sample Input 2
print(sum_of_integers(10, 1, 2))

# Sample Input 3
print(sum_of_integers(100, 4, 16))