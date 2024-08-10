def min_casts(N, M, sequences):
    cast_count = 0
    current_sequence = sequences[0]
    
    for i in range(1, N):
        if sequences[i] <= current_sequence:
            diff = current_sequence[0] - sequences[i][0] + 1
            cast_count += diff
            for j in range(M):
                current_sequence[j] += diff
        else:
            current_sequence = sequences[i]
    
    return cast_count if all(sequences[i] < sequences[i+1] for i in range(N-1)) else -1
N, M = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(N)]
print(min_casts(N, M, sequences))