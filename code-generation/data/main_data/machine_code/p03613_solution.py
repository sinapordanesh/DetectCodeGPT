def maximize_count(N, arr):
    X = max(set(arr), key = arr.count)
    return arr.count(X)

#Sample Input 1
print(maximize_count(7, [3, 1, 4, 1, 5, 9, 2]))

#Sample Input 2
print(maximize_count(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

#Sample Input 3
print(maximize_count(1, [99999]))