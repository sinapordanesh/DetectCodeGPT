def magic_square(A, B, C):
    D = 15 - A - B - C
    return f"{A} {B} {D}\n{C} {D} {B}\n{D} {C} {A}"

# Sample Input 1
print(magic_square(8, 3, 5))

# Sample Input 2
print(magic_square(1, 1, 1))