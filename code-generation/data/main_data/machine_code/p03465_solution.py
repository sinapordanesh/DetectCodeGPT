def find_median(N, A):
    from itertools import combinations
    
    sums = []
    for i in range(1, N+1):
        for subset in combinations(A, i):
            sums.append(sum(subset))
    
    sums.sort()
    return sums[(2**(N-1))-1]