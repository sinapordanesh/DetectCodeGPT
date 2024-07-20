def ways_to_transform(N, copies):
    total_ways = 0
    for i in range(1, 2**N):
        transformed_copies = set()
        for j in range(N):
            if (i >> j) & 1:
                transformed_copies.add(copies[j])
        if len(transformed_copies) == len(copies) and all(copy[1] < 0 for copy in transformed_copies):
            total_ways += 1
    return total_ways % (10**9 + 7)