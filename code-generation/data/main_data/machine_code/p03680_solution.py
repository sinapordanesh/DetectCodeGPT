def gain_muscle(N, a):
    count = 0
    current = 1
    while True:
        count += 1
        current = a[current-1]
        if current == 2:
            return count
        if count > N:
            return -1

# Sample Input 1
print(gain_muscle(3, [3, 1, 2]))

# Sample Input 2
print(gain_muscle(4, [3, 4, 1, 2]))

# Sample Input 3
print(gain_muscle(5, [3, 3, 4, 2, 4]))