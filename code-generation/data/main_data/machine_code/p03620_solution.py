def min_operations(A, B):
    if A == B:
        return 0
    
    if '1' not in B:
        return -1
    
    n = len(A)
    min_ops = float('inf')
    
    for i in range(n):
        if B[i] == '1':
            ops = 0
            temp_A = A
            for j in range(n):
                if temp_A == B:
                    min_ops = min(min_ops, ops)
                    break
                if temp_A[j] != B[j]:
                    temp_A = temp_A[:j] + str(1-int(temp_A[j])) + temp_A[j+1:]
                    ops += 1
            if temp_A == B:
                min_ops = min(min_ops, ops)
    
    return min_ops

# Input
A = "1010"
B = "1100"

# Output
print(min_operations(A, B))