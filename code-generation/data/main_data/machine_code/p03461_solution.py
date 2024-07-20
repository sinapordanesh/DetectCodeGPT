def construct_graph(A, B, distances):
    for x in range(1, A+1):
        for y in range(1, B+1):
            if distances[x-1][y-1] != min(distances[x-1]) + min([distances[i][y-1] for i in range(A)]):
                print("Impossible")
                return
    print("Possible")
    N = A + B
    M = A*B + A + B
    print(N, M)
    for i in range(1, A+1):
        print(i, A+1, "X")
    for i in range(A+1, N):
        print(i, A+1, "Y")
    for i in range(1, A):
        for j in range(1, B+1):
            print(i, A+j, distances[i-1][j-1])
    for j in range(1, B):
        for i in range(1, A+1):
            print(A+j, i, distances[i-1][j-1])
    print(1, N)
    return

# Sample Input 1
# A = 2, B = 3
# distances = [[1, 2, 2], [1, 2, 3]]
# construct_graph(2, 3, [[1, 2, 2], [1, 2, 3])

# Sample Input 2
# A = 1, B = 3
# distances = [[100, 50, 1]]
# construct_graph(1, 3, [[100, 50, 1]])