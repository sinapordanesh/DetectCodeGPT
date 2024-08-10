def smallest_number_of_rounds(N, A, B):
    diff = abs(B - A)
    if diff % 2 == 0:
        return diff // 2
    else:
        return min(A - 1, N - B) + (diff - 1) // 2

# Sample Input 1
print(smallest_number_of_rounds(5, 2, 4))

# Sample Input 2
print(smallest_number_of_rounds(5, 2, 3))