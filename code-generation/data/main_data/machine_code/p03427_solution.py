def max_digit_sum(N):
    max_sum = 0
    for n in range(N, 0, -1):
        temp_sum = sum(int(i) for i in str(n))
        if temp_sum > max_sum:
            max_sum = temp_sum
    print(max_sum)

# Test the function with sample inputs
max_digit_sum(100)
max_digit_sum(9995)
max_digit_sum(3141592653589793)