def kth_smallest_integer(N, K, operations):
    array = []
    for i in range(N):
        a, b = operations[i]
        array += [a] * b
    array.sort()
    return array[K-1]