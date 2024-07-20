def compare_hexadecimal(X, Y):
    hex_values = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    
    if hex_values[X] < hex_values[Y]:
        return "<"
    elif hex_values[X] > hex_values[Y]:
        return ">"
    else:
        return "="

# Sample Input 1
print(compare_hexadecimal('A', 'B'))

# Sample Input 2
print(compare_hexadecimal('E', 'C'))

# Sample Input 3
print(compare_hexadecimal('F', 'F'))