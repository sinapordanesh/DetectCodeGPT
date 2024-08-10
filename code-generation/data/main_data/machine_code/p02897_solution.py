def probability_of_odd(N):
    odd = (N + 1) // 2
    return odd / N

N = int(input())
print("{:.10f}".format(probability_of_odd(N)))