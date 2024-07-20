def sum_after_operations(N, A, Q, queries):
    total_sum = sum(A)
    current_dict = dict(zip(range(1, N+1), A))
    result = [total_sum]
    
    for i in range(Q):
        b, c = queries[2*i], queries[2*i+1]
        for key, value in current_dict.items():
            if value == b:
                total_sum += (c - b)
                current_dict[key] = c
        result.append(total_sum)
    
    return result[1:]