def immediate_subordinates(N, boss_list):
    subordinates = [0] * (N + 1)
    for i in range(2, N + 1):
        subordinates[boss_list[i-2]] += 1
    for i in range(1, N + 1):
        print(subordinates[i])

# Test the function with Sample Input 1
immediate_subordinates(5, [1, 1, 2, 2])
# Test the function with Sample Input 2
immediate_subordinates(10, [1, 1, 1, 1, 1, 1, 1, 1, 1])
# Test the function with Sample Input 3
immediate_subordinates(7, [1, 2, 3, 4, 5, 6])