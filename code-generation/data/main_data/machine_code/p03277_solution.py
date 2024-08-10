import statistics

def median_of_medians(N, a):
    m = []
    for i in range(N):
        for j in range(i, N):
            m.append(statistics.median(a[i:j+1]))
    return statistics.median(m)

# Sample Input 1
print(median_of_medians(3, [10, 30, 20]))

# Sample Input 2
print(median_of_medians(1, [10]))

# Sample Input 3
print(median_of_medians(10, [5, 9, 5, 9, 8, 9, 3, 5, 4, 3]))