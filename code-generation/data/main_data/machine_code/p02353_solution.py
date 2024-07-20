def RSQ_RUQ(n, q, queries):
    arr = [0] * n
    
    def update(s, t, x):
        for i in range(s, t+1):
            arr[i] = x
    
    def getSum(s, t):
        return sum(arr[s:t+1])
    
    result = []
    for query in queries:
        if query[0] == 0:
            update(query[1], query[2], query[3])
        else:
            result.append(getSum(query[1], query[2]))
    
    return result

# Sample Input
n = 6
q = 7
queries = [(0, 1, 3, 1), (0, 2, 4, -2), (1, 0, 5), (1, 0, 1), (0, 3, 5, 3), (1, 3, 4), (1, 0, 5)]

# Sample Output
print(RSQ_RUQ(n, q, queries))