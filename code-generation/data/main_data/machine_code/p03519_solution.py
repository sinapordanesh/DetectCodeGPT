def max_beauty(N, Q, a, b, queries):
    def calculate_beauty(a, b):
        total = 0
        for i in range(2*N):
            if s[i] == t[i]:
                total += a[i]
            else:
                total += b[i]
        return total
    
    result = []
    for p, x, y in queries:
        a[p-1] = x
        b[p-1] = y
        s = "(" * N + ")" * N
        t = "(" * N + ")" * N
        result.append(calculate_beauty(a, b))
    
    return result

# Sample Input 1
N = 2
Q = 2
a = [1, 1, 7, 3]
b = [4, 2, 3, 3]
queries = [(2, 4, 6), (3, 2, 5)]
print(*max_beauty(N, Q, a, b, queries))

# Sample Input 2
N = 7
Q = 7
a = [34, -20, -27, 42, 44, 29, 9, 11, 20, 44, 27, 19, -31, -29]
b = [46, -50, -11, 20, 28, 46, 12, 13, 33, -22, -48, -27, 35, -17]
queries = [(7, 27, 34), (12, -2, 22), (4, -50, -12), (3, -32, 15), (8, -7, 23), (3, -30, 11), (4, -2, 23)]
print(*max_beauty(N, Q, a, b, queries))