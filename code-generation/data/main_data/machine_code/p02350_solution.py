def RMQ_RUQ(n, queries):
    arr = [2**31-1] * n
    result = []
    
    for query in queries:
        if query[0] == 0:
            for i in range(query[1], query[2]+1):
                arr[i] = query[3]
        elif query[0] == 1:
            result.append(min(arr[query[1]:query[2]+1]))
    
    return result

# Sample Input 1
n = 3
queries = [(0, 0, 1, 1), (0, 1, 2, 3), (0, 2, 2, 2), (1, 0, 2), (1, 1, 2)]
print(RMQ_RUQ(n, queries))

# Sample Input 2
n = 1
queries = [(1, 0, 0), (0, 0, 0, 5), (1, 0, 0)]
print(RMQ_RUQ(n, queries))