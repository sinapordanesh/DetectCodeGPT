def sequence_operations(N, b):
    a = []
    for i in range(N):
        if b[i] > i + 1:
            return -1
        a.insert(b[i]-1, b[i])
    return a

N = 3
b = [1, 2, 1]
print(*sequence_operations(N, b))

N = 2
b = [2, 2]
print(*sequence_operations(N, b))

N = 9
b = [1, 1, 1, 2, 2, 1, 2, 3, 2]
print(*sequence_operations(N, b))