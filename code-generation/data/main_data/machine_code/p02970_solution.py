def min_inspectors_needed(N, D):
    inspectors = [0] * (N+1)
    for i in range(1, N+1):
        inspectors[i] = min(inspectors[max(0, i-D)] + 1, inspectors[i])
        inspectors[min(N, i+D)] = min(inspectors[min(N, i+D)], inspectors[i] + 1)
    return inspectors[N]

N, D = map(int, input().split())
print(min_inspectors_needed(N, D))