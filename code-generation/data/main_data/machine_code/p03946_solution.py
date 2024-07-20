def min_cost_to_decrease_profit(N, T, A):
    A_sorted = sorted(A)
    diff = [A_sorted[i+1] - A_sorted[i] for i in range(N-1)]
    diff_sorted = sorted(diff)

    result = sum(diff_sorted[:N-1-(T-1)]) if T < N else 0

    return result

# Sample Input 1
print(min_cost_to_decrease_profit(3, 2, [100, 50, 200]))

# Sample Input 2
print(min_cost_to_decrease_profit(5, 8, [50, 30, 40, 10, 20]))

# Sample Input 3
print(min_cost_to_decrease_profit(10, 100, [7, 10, 4, 5, 9, 3, 6, 8, 2, 1]))