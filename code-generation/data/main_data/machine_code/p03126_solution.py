def common_foods(N, M, likes):
    count = 0
    for food in range(1, M+1):
        if all(food in liked_foods for liked_foods in likes):
            count += 1
    return count

# Sample Input 1
# N, M = 3, 4
# likes = [[1, 3], [1, 2, 3], [3, 2]]
# print(common_foods(N, M, likes))

# Sample Input 2
# N, M = 5, 5
# likes = [[2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4]]
# print(common_foods(N, M, likes))

# Sample Input 3
# N, M = 1, 30
# likes = [[5, 10, 30]]
# print(common_foods(N, M, likes))