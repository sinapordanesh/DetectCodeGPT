def num_operations(N, arr):
    max_num = max(arr)
    count = 0
    while max_num >= N:
        max_num_index = arr.index(max_num)
        arr[max_num_index] -= N
        for i in range(N):
            if i != max_num_index:
                arr[i] += 1
        count += 1
        max_num = max(arr)
    return count

#Sample Input
print(num_operations(4, [3, 3, 3, 3]))
print(num_operations(3, [1, 0, 3]))
print(num_operations(2, [2, 2]))
print(num_operations(7, [27, 0, 0, 0, 0, 0, 0]))
print(num_operations(10, [1000, 193, 256, 777, 0, 1, 1192, 1234567891011, 48, 425]))