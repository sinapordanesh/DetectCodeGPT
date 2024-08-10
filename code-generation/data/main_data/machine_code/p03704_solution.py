def count_positive_integers(D):
    count = 0
    for N in range(1, 10**6 + 1):
        if int(str(N)[::-1]) == N + D:
            count += 1
    return count

D = int(input().strip())
print(count_positive_integers(D))