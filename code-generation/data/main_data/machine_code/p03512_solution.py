def largest_term(Q, operations):
    sequence = [0] * 301
    for i in range(Q):
        m_i, x_i = operations[i]
        for j in range(1, 301):
            sequence[j*m_i] += x_i
    return max(sequence)

# Sample Input 1
Q = 3
operations = [(2, 10), (3, -20), (6, 15)]
print(largest_term(Q, operations))

# Sample Input 2
Q = 3
operations = [(10, -3), (50, 4), (100, -5)]
print(largest_term(Q, operations))

# Sample Input 3
Q = 5
operations = [(56, 114834), (72, -149861), (100, 190757), (192, -132693), (240, 133108)]
print(largest_term(Q, operations))