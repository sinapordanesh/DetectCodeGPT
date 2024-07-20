def hierarchical_calculator(N, a):
    from itertools import combinations
    
    max_val = 0
    result = []
    
    for k in range(1, N+1):
        for indices in combinations(range(1, N+1), k):
            x = 1
            for idx in indices:
                x *= a[idx-1]
            if x > max_val:
                max_val = x
                result = list(indices)
            elif x == max_val:
                if len(indices) < len(result):
                    result = list(indices)
                elif len(indices) == len(result) and indices < result:
                    result = list(indices)
    
    print(len(result))
    for idx in result:
        print(idx)