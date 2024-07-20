def find_different_number(A, B, C):
    if A == B:
        return C
    elif A == C:
        return B
    else:
        return A

# Test the function with sample inputs
print(find_different_number(5, 7, 5))
print(find_different_number(1, 1, 7))
print(find_different_number(-100, 100, 100))