def max_participants(Q, queries):
    for query in queries:
        A, B = query
        score = A*B
        count = 0
        for i in range(1, int(score**0.5)+1):
            if A >= i and B >= i and A <= score//i and B <= score//i:
                count += 1
        print(count)
        
# Sample Input
max_participants(8, [(1, 4), (10, 5), (3, 3), (4, 11), (8, 9), (22, 40), (8, 36), (314159265, 358979323)])