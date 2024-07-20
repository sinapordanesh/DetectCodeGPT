def find_integer_sequence(N, x):
    a = [0] * (N**2)
    for i in range(N):
        a[x[i]-1] = i+1
    result = []
    for i in range(N):
        for j in range(N):
            result.append(a[i]+1)
    for i in range(N):
        for j in range(N):
            result[i*N+j] = a[i]
    if len(set(result)) != N**2:
        print("No")
    else:
        print("Yes")
        print(" ".join(map(str, result)))