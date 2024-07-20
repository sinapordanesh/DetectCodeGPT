def count_elements(n, p):
    count = 0
    for i in range(1, n-1):
        if p[i] == sorted([p[i-1], p[i], p[i+1]])[1]:
            count += 1
    return count

# Sample Input 1
# n = 5
# p = [1, 3, 5, 4, 2]
# Sample Output 1
# print(count_elements(5, [1, 3, 5, 4, 2]))

# Sample Input 2
# n = 9
# p = [9, 6, 3, 2, 5, 8, 7, 4, 1]
# Sample Output 2
# print(count_elements(9, [9, 6, 3, 2, 5, 8, 7, 4, 1]))