def RSQ_RAQ(n, queries):
    A = [0] * n
    result = []
    
    def add(s, t, x):
        for i in range(s-1, t):
            A[i] += x
    
    def getSum(s, t):
        result.append(sum(A[s-1:t]))
    
    for query in queries:
        q = query.split()
        if q[0] == '0':
            add(int(q[1]), int(q[2]), int(q[3]))
        elif q[0] == '1':
            getSum(int(q[1]), int(q[2]))
    
    return result

# Sample Input 1
n = 3
queries = ['0 1 2 1', '0 2 3 2', '0 3 3 3', '1 1 2', '1 2 3']
print(RSQ_RAQ(n, queries))

# Sample Input 2
n = 4
queries = ['1 1 4', '0 1 4 1', '1 1 4']
print(RSQ_RAQ(n, queries))