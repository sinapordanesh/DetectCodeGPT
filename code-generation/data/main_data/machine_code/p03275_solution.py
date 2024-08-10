def median_of_medians(a):
    n = len(a)
    m = []
    for i in range(n):
        for j in range(i, n):
            subsequence = a[i:j+1]
            subsequence.sort()
            median = subsequence[(len(subsequence) -1)//2]
            m.append(median)
    m.sort()
    return m[(len(m) - 1)//2]

#Sample Input 1
a = [10, 30, 20]
print(median_of_medians(a))

#Sample Input 2
a = [10]
print(median_of_medians(a))

#Sample Input 3
a = [5, 9, 5, 9, 8, 9, 3, 5, 4, 3]
print(median_of_medians(a))