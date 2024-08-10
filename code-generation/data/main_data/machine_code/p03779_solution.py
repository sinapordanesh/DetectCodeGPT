def kangaroo_jump(X):
    total = 0
    jump = 1
    while total < X or (total - X) % 2 != 0:
        total += jump
        jump += 1
    return jump

# Test the function with the sample inputs
print(kangaroo_jump(6))
print(kangaroo_jump(2))
print(kangaroo_jump(11))