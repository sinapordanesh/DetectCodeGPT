def maximum_euclidean_step_count(Q, queries):
    MOD = 10**9 + 7
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def euclidean_step_count(a, b):
        if a == 0:
            return 0
        if a > b:
            a, b = b, a
        count = 1
        while b % a != 0:
            q = b // a
            a, b = b % a, a
            count += 1
        return count
    
    for query in queries:
        X, Y = query
        max_step_count = 0
        pairs_with_max_count = 0
        
        for x in range(1, X + 1):
            for y in range(1, Y + 1):
                step_count = euclidean_step_count(x, y)
                if step_count > max_step_count:
                    max_step_count = step_count
                    pairs_with_max_count = 1
                elif step_count == max_step_count:
                    pairs_with_max_count += 1
        
        print(max_step_count, pairs_with_max_count % MOD)