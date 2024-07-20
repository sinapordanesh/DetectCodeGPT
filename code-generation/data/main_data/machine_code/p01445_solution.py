def maximal_bandwidth(N, M, data):
    for i in range(N):
        for j in range(N):
            if i != j:
                data[i][j] = "0"

    for i in range(N):
        for j in range(N):
            for k in range(N):
                data[j][k] = max(data[j][k], data[j][i] + data[i][k])

    print(data[0][-1])

# Sample Input
N = 3
M = 3
data = [["0" for _ in range(N)] for _ in range(N)]
data[0][1] = "x+2"
data[1][2] = "2x+1"
data[2][0] = "x+1"

maximal_bandwidth(N, M, data)