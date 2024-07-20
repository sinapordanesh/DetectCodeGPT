def min_watering_operations(N, h):
    operations = 0
    for i in range(N-1):
        if h[i] < h[i+1]:
            operations += h[i+1] - h[i]
    return operations

#Sample Input 1
print(min_watering_operations(4, [1, 2, 2, 1]))

#Sample Input 2
print(min_watering_operations(5, [3, 1, 2, 3, 1]))

#Sample Input 3
print(min_watering_operations(8, [4, 23, 75, 0, 23, 96, 50, 100]))