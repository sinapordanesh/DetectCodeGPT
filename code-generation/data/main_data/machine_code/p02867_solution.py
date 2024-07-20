def possible_to_swap(N, A, B):
    diff_count = 0
    for i in range(N):
        if A[i] > B[i]:
            diff_count += 1
        if diff_count > 2:
            return "No"
    return "Yes" 

# Test the function with sample inputs
print(possible_to_swap(3, [1, 3, 2], [1, 2, 3]))
print(possible_to_swap(3, [1, 2, 3], [2, 2, 2]))
print(possible_to_swap(6, [3, 1, 2, 6, 3, 4], [2, 2, 8, 3, 4, 3]))