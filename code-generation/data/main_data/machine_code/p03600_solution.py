def shortest_possible_total_length_of_roads(N, A):
    shortest_total_length = -1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if A[i][j] > A[i][k] + A[k][j]:
                    return shortest_total_length
    shortest_total_length = sum([sum(row) for row in A]) // 2
    return shortest_total_length

# Sample Input 1
N = 3
A = [[0, 1, 3], [1, 0, 2], [3, 2, 0]]
print(shortest_possible_total_length_of_roads(N, A))

# Sample Input 2
N = 3
A = [[0, 1, 3], [1, 0, 1], [3, 1, 0]]
print(shortest_possible_total_length_of_roads(N, A))

# Sample Input 3
N = 5
A = [[0, 21, 18, 11, 28], [21, 0, 13, 10, 26], [18, 13, 0, 23, 13], [11, 10, 23, 0, 17], [28, 26, 13, 17, 0]]
print(shortest_possible_total_length_of_roads(N, A))

# Sample Input 4
N = 3
A = [[0, 1000000000, 1000000000], [1000000000, 0, 1000000000], [1000000000, 1000000000, 0]]
print(shortest_possible_total_length_of_roads(N, A))