def count_tuples(N):
    count = 0
    for A in range(1, N):
        for B in range(1, N):
            if (A * B + N) % A == 0:
                count += 1
    return count

N = int(input())
print(count_tuples(N))