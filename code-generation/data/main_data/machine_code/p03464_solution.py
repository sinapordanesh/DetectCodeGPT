def calculate_possible_number_of_children(K, A):
    min_children = 2
    max_children = 10 ** 9
    
    for a in A:
        min_children = ((min_children + a - 1) // a) * a
        max_children = (max_children // a) * a
    
    if min_children > max_children:
        return -1
    else:
        return min_children, max_children

# Sample Input 1
print(calculate_possible_number_of_children(4, [3, 4, 3, 2]))

# Sample Input 2
print(calculate_possible_number_of_children(5, [3, 4, 100, 3, 2]))

# Sample Input 3
print(calculate_possible_number_of_children(10, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))