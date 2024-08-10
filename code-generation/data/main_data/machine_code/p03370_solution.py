def max_num_doughnuts(N, X, m):
    total_moto = sum(m)
    remaining_moto = X - total_moto
    min_doughnuts = N + remaining_moto // min(m)
    return min(min_doughnuts, X // min(m))  

#Input reading
inputs = list(map(int, input().split()))
N = inputs[0]
X = inputs[1]
m = inputs[2:]

#Function call
result = max_num_doughnuts(N, X, m)
print(result)