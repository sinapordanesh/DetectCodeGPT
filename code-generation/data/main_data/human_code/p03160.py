import numpy as np

def chmin(a,b):
    a = a if a < b else b

    return a

def chmax(a, b):
    a = a if a > b else b

    return a


N = int(input().strip())

h_point = []
temp = input().split()
for i in range(N):
    h_point.append(int(temp[i]))

costs = [0, abs(h_point[1]-h_point[0])]
for i in range(2, N):
    ans_temp = chmin(costs[i-1]+abs(h_point[i]-h_point[i-1]), costs[i-2]+abs(h_point[i]-h_point[i-2]))
    costs.append(ans_temp)

print(costs[N-1])