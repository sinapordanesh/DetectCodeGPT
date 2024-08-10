def find_final_sequence(n, a):
    b = []
    for i in range(n):
        b.append(a[i])
        b.reverse()
    return b

# Sample Input 1
print(*find_final_sequence(4, [1, 2, 3, 4]))

# Sample Input 2
print(*find_final_sequence(3, [1, 2, 3]))

# Sample Input 3
print(*find_final_sequence(1, [1000000000]))

# Sample Input 4
print(*find_final_sequence(6, [0, 6, 7, 6, 7, 0]))