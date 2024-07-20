def max_score(N, arr):
    arr.sort()
    first_half = sum(arr[:N+N])
    second_half = sum(arr[N+N:])
    return first_half - second_half

N = 2
arr = [3, 1, 4, 1, 5, 9]
print(max_score(N, arr))

N = 1
arr = [1, 2, 3]
print(max_score(N, arr))

N = 3
arr = [8, 2, 2, 7, 4, 6, 5, 3, 8]
print(max_score(N, arr))