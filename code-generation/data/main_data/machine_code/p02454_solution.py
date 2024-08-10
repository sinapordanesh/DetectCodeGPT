def equal_range(n, A, q, queries):
    for k in queries:
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if A[m] < k:
                l = m + 1
            else:
                r = m
        lb = l
        
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if A[m] <= k:
                l = m + 1
            else:
                r = m
        ub = l
        
        print(lb, ub)  

# Sample Input
n = 4
A = [1, 2, 2, 4]
q = 3
queries = [2, 3, 5]
equal_range(n, A, q, queries)