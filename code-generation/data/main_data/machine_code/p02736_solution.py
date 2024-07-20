def find_x(N, A):
    x = [int(digit) for digit in A]
    for i in range(2, N+1):
        new_x = []
        for j in range(N+1-i):
            new_x.append(abs(x[j] - x[j+1]))
        x = new_x
    return x[0]

# Sample Input 1
print(find_x(4, "1231"))

# Sample Input 2
print(find_x(10, "2311312312"))