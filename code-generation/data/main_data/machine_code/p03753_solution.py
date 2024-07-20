def max_meetings(n, m, a):
    count = 0
    for i in range(1, n):
        if a[i] - a[i-1] == 1:
            count += 1
    return count

# Sample Input 1
print(max_meetings(7, 7, [1, 3, 5]))

# Sample Input 2
print(max_meetings(10, 14, [5, 6, 7, 8, 9, 10, 11, 12]))