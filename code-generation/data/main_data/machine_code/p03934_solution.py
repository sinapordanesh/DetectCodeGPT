def sushi_counter(N, Q, customers):
    dishes = [0] * N
    eaten = [0] * N
    total_eaten = 0
    
    for customer in customers:
        for i in range(N):
            if eaten[i] < customer[1]:
                dishes[i] += 1
                total_eaten += 1
                eaten[i] += 1
            if total_eaten >= Q:
                break
    
    return dishes

# Sample Input 1
print(sushi_counter(9, 3, [(5, 11), (8, 4), (4, 7)]))

# Sample Input 2
print(sushi_counter(6, 6, [(3, 5), (6, 11), (1, 6), (4, 7), (5, 2), (2, 5)]))

# Sample Input 3
print(sushi_counter(5, 6, [(1, 1), (2, 1), (3, 1), (1, 1), (5, 1), (3, 1)]))

# Sample Input 4
print(sushi_counter(10, 10, [(10, 10), (9, 20), (8, 30), (7, 40), (6, 50), (5, 60), (4, 70), (3, 80), (2, 90), (1, 100)]))