def find_maximum_value(N, arr):
    for i in range(N):
        temp = arr[:i] + arr[i+1:]
        print(max(temp))

# Sample Input 1
find_maximum_value(3, [1, 4, 3])

# Sample Input 2
find_maximum_value(2, [5, 5])