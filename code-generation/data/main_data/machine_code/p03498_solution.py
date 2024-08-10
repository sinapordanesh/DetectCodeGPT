def operate(N, a):
    operations = []
    while not all(a[i] <= a[i+1] for i in range(N-1)):
        max_val = max(a)
        max_idx = a.index(max_val)
        min_val = min(a)
        min_idx = a.index(min_val)
        if max_val - min_val <= 1:
            break
        operations.append((max_idx+1, min_idx+1))
        a[min_idx] += max_val
    print(len(operations))
    for op in operations:
        print(op[0], op[1]) 

# Sample Input 1
operate(3, [-2, 5, -1])

# Sample Input 2
operate(2, [-1, -3])

# Sample Input 3
operate(5, [0, 0, 0, 0, 0])