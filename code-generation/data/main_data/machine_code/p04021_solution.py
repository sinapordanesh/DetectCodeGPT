def min_operations_to_sort_sequence(N, sequence):
    count = 0
    idx = 0
    for i in range(N):
        if sequence[i] == idx + 1:
            idx += 1
        else:
            count += 1
    return count - 1 if count != 0 else 0

#Sample Input 1
print(min_operations_to_sort_sequence(4, [2, 4, 3, 1])) #Output: 1

#Sample Input 2
print(min_operations_to_sort_sequence(5, [10, 8, 5, 3, 2])) #Output: 0