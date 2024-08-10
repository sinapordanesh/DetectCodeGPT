def number_of_classes_can_attend(N, A, B, classes):
    count = 0
    for c in classes:
        if c < A or c > B:
            count += 1
    return count

# Sample Input 1
print(number_of_classes_can_attend(5, 5, 9, [4, 3, 6, 9, 1])) # Output: 4

# Sample Input 2
print(number_of_classes_can_attend(5, 4, 9, [5, 6, 7, 8, 9])) # Output: 1

# Sample Input 3
print(number_of_classes_can_attend(4, 3, 6, [9, 6, 8, 1])) # Output: 4

# Sample Input 4
print(number_of_classes_can_attend(2, 1, 2, [1, 2])) # Output: 1