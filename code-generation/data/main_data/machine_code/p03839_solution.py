def max_possible_score(N, K, arr):
    max_sum = 0
    for i in range(N - K + 1):
        sum_black = sum(arr[i:i+K])
        max_sum = max(max_sum, sum_black)
    return max_sum

# Sample Input 1
print(max_possible_score(5, 3, [-10, 10, -10, 10, -10]))

# Sample Input 2
print(max_possible_score(4, 2, [10, -10, -10, 10]))

# Sample Input 3
print(max_possible_score(1, 1, [-10]))

# Sample Input 4
print(max_possible_score(10, 5, [5, -4, -5, -8, -4, 7, 2, -4, 0, 7]))