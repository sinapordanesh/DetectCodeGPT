def find_median(N, X):
    X.sort()
    medians = []
    
    for i in range(N):
        temp = X[:i] + X[i+1:]
        temp.sort()
        if len(temp) % 2 == 0:
            medians.append(temp[len(temp)//2 - 1])
        else:
            medians.append(temp[len(temp)//2])
    
    return medians

N = 4
X = [2, 4, 4, 3]
output = find_median(N, X)
for value in output:
    print(value)

N = 2
X = [1, 2]
output = find_median(N, X)
for value in output:
    print(value)

N = 6
X = [5, 5, 4, 4, 3, 3]
output = find_median(N, X)
for value in output:
    print(value)