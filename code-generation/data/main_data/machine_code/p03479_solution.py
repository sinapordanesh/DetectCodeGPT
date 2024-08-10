def max_sequence_length(X, Y):
    max_length = 1
    for i in range(X, Y+1):
        length = 1
        num = i
        while num * 2 <= Y:
            num *= 2
            length += 1
        max_length = max(max_length, length)
    return max_length

X, Y = map(int, input().split())
print(max_sequence_length(X, Y))