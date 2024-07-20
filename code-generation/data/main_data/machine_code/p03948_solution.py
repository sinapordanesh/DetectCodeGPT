def minimum_cost(N, T, A):
    A_sorted = sorted(A)
    diff = [a - b for a, b in zip(A_sorted[1:], A_sorted[:-1])]
    diff.sort()
    return sum(diff[:N-1])

#Sample Input 1
print(minimum_cost(3, 2, [100, 50, 200]))

#Sample Input 2
print(minimum_cost(5, 8, [50, 30, 40, 10, 20]))

#Sample Input 3
print(minimum_cost(10, 100, [7, 10, 4, 5, 9, 3, 6, 8, 2, 1]))