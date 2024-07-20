def process_queries(Q, queries):
    f = 0
    for query in queries:
        if query[0] == 1:
            a, b = query[1], query[2]
            f = f + abs(x - a) + b
        elif query[0] == 2:
            x = 0
            min_val = float('inf')
            for i in range(-10**9, 10**9+1):
                val = f + abs(i - a)
                if val < min_val:
                    min_val = val
                    x = i
            print(x, min_val)