import math

def diverse_city(N):
    roads = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            roads[i][j] = roads[j][i] = 111 * (i+j+2) 
            
    for row in roads:
        print(*row)

N = 4
diverse_city(N)