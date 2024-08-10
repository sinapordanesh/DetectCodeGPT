def total_rectangle_area(n, m, x_values, y_values):
    MOD = 10**9 + 7
    x_values.sort()
    y_values.sort()
    
    total_area = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(1, m):
                for l in range(k+1, m):
                    area = (x_values[j] - x_values[i]) * (y_values[l] - y_values[k])
                    total_area = (total_area + area) % MOD
    
    return total_area

# Sample Input 1
print(total_rectangle_area(3, 3, [1, 3, 4], [1, 3, 6]))

# Sample Input 2
print(total_rectangle_area(6, 5, [-790013317, -192321079, 95834122, 418379342, 586260100, 802780784], [-253230108, 193944314, 363756450, 712662868, 735867677]))