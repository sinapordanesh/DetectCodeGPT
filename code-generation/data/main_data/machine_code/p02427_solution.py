def enumeration_of_subsets(n):
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j)
        print(f"{i}: {' '.join(map(str, subset))}")

n = 4
enumeration_of_subsets(n)