def maximum_customers_served(N, customers):
    count = 0
    for i in range(N):
        if customers[i][0] <= 5 and customers[i][2] <= 11 and customers[i][4] <= 17:
            count += 1
    return count

# Sample Input
N = 5
customers = [[1, 0, 2, 0, 3, 30, 4, 30, 6, 0, 7, 0],
             [2, 30, 3, 0, 4, 0, 5, 0, 5, 30, 6, 30],
             [1, 30, 2, 30, 4, 30, 5, 0, 6, 30, 7, 0],
             [2, 30, 3, 0, 5, 0, 6, 0, 6, 30, 7, 0],
             [1, 0, 2, 0, 3, 0, 3, 30, 4, 0, 5, 0]]

print(maximum_customers_served(N, customers))