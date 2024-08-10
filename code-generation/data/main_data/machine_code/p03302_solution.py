def determine_sum_or_product(a, b):
    if a + b == 15:
        return "+"
    elif a * b == 15:
        return "*"
    else:
        return "x"

# Test the function with the provided sample inputs
print(determine_sum_or_product(4, 11))
print(determine_sum_or_product(3, 5))
print(determine_sum_or_product(1, 1))