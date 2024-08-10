def construct_sequence(M, K):
    sequence = []
    for i in range(2**M):
        sequence.append(i)
        sequence.append(i)
    result = []
    for i in range(len(sequence)):
        temp = 0
        for j in range(i, len(sequence)):
            temp ^= sequence[j]
            if temp == K:
                result = sequence[i:j+1]
                break
        if result:
            break
    return result