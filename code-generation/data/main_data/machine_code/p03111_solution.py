def magic_points(N, A, B, C, lengths):
    lengths.sort(reverse=True)
    mp = 0
    while A not in lengths or B not in lengths or C not in lengths:
        if A not in lengths:
            if max(lengths) > A:
                lengths[lengths.index(max(lengths))] -= 1
                mp += 1
            else:
                lengths.append(A)
        if B not in lengths:
            if max(lengths) > B:
                lengths[lengths.index(max(lengths))] -= 1
                mp += 1
            else:
                lengths.append(B)
        if C not in lengths:
            if max(lengths) > C:
                lengths[lengths.index(max(lengths))] -= 1
                mp += 1
            else:
                lengths.append(C)
        lengths.sort(reverse=True)
        if A not in lengths or B not in lengths or C not in lengths:
            if len(lengths) >= 2:
                lengths.append(lengths.pop() + lengths.pop())
                mp += 10
    return mp

# Input
input_values = list(map(int, input().split()))
N, A, B, C = input_values[:4]
lengths = input_values[4:]

# Output
print(magic_points(N, A, B, C, lengths))