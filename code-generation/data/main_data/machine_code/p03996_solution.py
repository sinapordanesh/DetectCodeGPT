def check_arrays(N, M, Q, operations):
    arrays = [[i for i in range(1, M+1)] for _ in range(N)]
    
    for op in operations:
        array_idx = op - 1
        arrays[array_idx] = [arrays[array_idx][op-1]] + arrays[array_idx][:op-1] + arrays[array_idx][op:]
    
    first_array = arrays[0]
    
    for arr in arrays:
        if arr != first_array:
            return "No"
    
    return "Yes"