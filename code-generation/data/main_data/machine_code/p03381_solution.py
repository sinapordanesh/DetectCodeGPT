def find_median(N, X):
    X.sort()
    medians = []
    for i in range(N):
        if i % 2 == 0:
            medians.append(X[i // 2])
        else:
            medians.append(X[i // 2])
    return medians

N = 4
X = [2, 4, 4, 3]
result = find_median(N, X)
for median in result:
    print(median)

N = 2
X = [1, 2]
result = find_median(N, X)
for median in result:
    print(median)

N = 6
X = [5, 5, 4, 4, 3, 3]
result = find_median(N, X)
for median in result:
    print(median)