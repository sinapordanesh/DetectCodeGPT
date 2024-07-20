def sum_of_sequence(N, X, M):
    A = [X]
    next_val = X
    sum_sequence = X
    for i in range(N-1):
        next_val = (next_val ** 2) % M
        if next_val in A:
            start_index = A.index(next_val)
            cycle_length = len(A) - start_index
            remaining_steps = (N - i - 2) % cycle_length
            sum_cycle = sum(A[start_index:]) * ((N - i - 2) // cycle_length)
            sum_remaining = sum(A[start_index:start_index + remaining_steps])
            return sum_sequence + sum_cycle + sum_remaining
        A.append(next_val)
        sum_sequence += next_val
    return sum_sequence

N, X, M = map(int, input().split())
print(sum_of_sequence(N, X, M))