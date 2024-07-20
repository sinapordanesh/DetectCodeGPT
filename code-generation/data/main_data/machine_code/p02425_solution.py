def bit_flag(q, queries):
    state = 0
    output = []

    for query in queries:
        operation, flag = query

        if operation == 0:
            output.append((state >> flag) & 1)
        elif operation == 1:
            state = state | (1 << flag)
        elif operation == 2:
            state = state & ~(1 << flag)
        elif operation == 3:
            state = state ^ (1 << flag)
        elif operation == 4:
            output.append(1 if state == (1 << 64) - 1 else 0)
        elif operation == 5:
            output.append(1 if state > 0 else 0)
        elif operation == 6:
            output.append(1 if state == 0 else 0)
        elif operation == 7:
            output.append(bin(state).count('1'))
        elif operation == 8:
            output.append(state)

    return output

# Sample Input
q = 14
queries = [(1, 0), (1, 1), (1, 2), (2, 1), (0, 0), (0, 1), (0, 2), (0, 3), (3, 3), 4, 5, 6, 7, 8]
print(bit_flag(q, queries))