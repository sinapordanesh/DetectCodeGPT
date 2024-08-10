def min_operations(n, arr):
    operations = 0
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += arr[i]
        s2 += arr[i]
        if i % 2 == 0:
            if s1 <= 0:
                operations += abs(s1) + 1
                s1 = 1
            if s2 >= 0:
                operations += abs(s2) + 1
                s2 = -1
        else:
            if s1 >= 0:
                operations += abs(s1) + 1
                s1 = -1
            if s2 <= 0:
                operations += abs(s2) + 1
                s2 = 1
    return operations

n = int(input())
arr = list(map(int, input().split()))

print(min_operations(n, arr))