def select_bags(N, P, biscuits):
    count = 0
    
    for i in range(1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += biscuits[j]
        if total % 2 == P:
            count += 1
            
    return count

# Sample Input 1
print(select_bags(2, 0, [1, 3]))

# Sample Input 2
print(select_bags(1, 1, [50]))

# Sample Input 3
print(select_bags(3, 0, [1, 1, 1]))

# Sample Input 4
print(select_bags(45, 1, [17, 55, 85, 55, 74, 20, 90, 67, 40, 70, 39, 89, 91, 50, 16, 24, 14, 43, 24, 66, 25, 9, 89, 71, 41, 16, 53, 13, 61, 15, 85, 72, 62, 67, 42, 26, 36, 66, 4, 87, 59, 91, 4, 25, 26]))