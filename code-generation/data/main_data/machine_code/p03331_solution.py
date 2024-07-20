def minimum_digit_sum(N):
    min_sum = float('inf')
    for i in range(1, N):
        A = i
        B = N - i
        sum_digits = sum(map(int, str(A))) + sum(map(int, str(B)))
        min_sum = min(min_sum, sum_digits)
    return min_sum

N = int(input())
print(minimum_digit_sum(N))