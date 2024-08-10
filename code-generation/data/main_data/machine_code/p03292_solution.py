def min_total_cost():
    A = list(map(int, input().split()))
    A.sort()
    return max(0, 2 * A[1] - A[0] - A[2])

print(min_total_cost())