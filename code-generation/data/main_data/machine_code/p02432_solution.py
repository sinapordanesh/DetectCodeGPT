from collections import deque

def dynamic_array(q, queries):
    A = deque()
    
    for query in queries:
        if query[0] == 0:
            if query[1] == 0:
                A.appendleft(query[2])
            else:
                A.append(query[2])
        elif query[0] == 1:
            print(A[query[1]])
        else:
            if query[1] == 0:
                A.popleft()
            else:
                A.pop()

q = 11
queries = [(0, 0, 1), (0, 0, 2), (0, 1, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (0, 0, 4), (1, 0), (1, 1)]
dynamic_array(q, queries)