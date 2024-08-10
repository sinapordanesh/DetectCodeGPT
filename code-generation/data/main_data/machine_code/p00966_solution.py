def string_puzzle(n, a, b, q, hints_a, hints_b, positions):
    secret_string = ['?'] * n
    for hint in hints_a:
        secret_string[hint[0] - 1] = hint[1]
        
    for hint in hints_b:
        start = hint[0] - 1
        end = hint[1]
        if end == 0:
            continue
        length = end - start
        for i in range(length):
            secret_string[start + i] = secret_string[hint[0] + i]
    
    result = ''
    for pos in positions:
        result += secret_string[pos - 1]
    
    return result

# Sample Input 1
n1 = 9
a1 = 4
b1 = 5
q1 = 4
hints_a1 = [(3, 'C'), (4, 'I'), (7, 'C'), (9, 'P')]
hints_b1 = [(2, 1), (4, 0), (6, 2), (7, 0), (8, 4)]
positions1 = [8, 1, 9, 6]

print(string_puzzle(n1, a1, b1, q1, hints_a1, hints_b1, positions1))

# Sample Input 2
n2 = 1000000000
a2 = 1
b2 = 1
q2 = 2
hints_a2 = [(20171217, 'A')]
hints_b2 = [(3, 1)]
positions2 = [42, 987654321]

print(string_puzzle(n2, a2, b2, q2, hints_a2, hints_b2, positions2) )