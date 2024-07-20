def maximum_length_sequence(X, Y):
    max_length = 1
    for i in range(X, Y+1):
        for j in range(i, Y+1):
            count = 1
            num = i
            while num*j <= Y:
                num *= j
                count += 1
            max_length = max(max_length, count)
    return max_length

X, Y = map(int, input().split())
print(maximum_length_sequence(X, Y))