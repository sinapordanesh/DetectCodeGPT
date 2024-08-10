def max_sum_sequence(matrix):
    max_sum = float('-inf')
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    current_sum = 0
                    for x in range(i, k+1):
                        for y in range(j, l+1):
                            current_sum += matrix[x][y]
                    max_sum = max(max_sum, current_sum)
    
    return max_sum