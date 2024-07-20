def maximize_final_integer(N, A):
    A.sort()
    operations = []
    for i in range(N-1):
        x = A.pop()
        y = A.pop()
        A.append(x - y)
        operations.append((x, y))
    
    return A[0], operations

# Sample Input 1
N = 3
A = [1, -1, 2]
print(maximize_final_integer(N, A))

# Sample Input 2
N = 3
A = [1, 1, 1]
print(maximize_final_integer(N, A))