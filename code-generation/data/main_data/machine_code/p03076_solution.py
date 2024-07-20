def earliest_delivery_time(A, B, C, D, E):
    dishes = [A, B, C, D, E]
    time = 0
    for dish in sorted(dishes, reverse=True):
        time = (time + 9) // 10 * 10 + dish
    return time

# Sample Input 1
print(earliest_delivery_time(29, 20, 7, 35, 120))

# Sample Input 2
print(earliest_delivery_time(101, 86, 119, 108, 57))

# Sample Input 3
print(earliest_delivery_time(123, 123, 123, 123, 123))