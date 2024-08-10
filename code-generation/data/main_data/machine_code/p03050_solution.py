def find_sum_of_favorite_numbers(N):
    total = 0
    for m in range(1, int(N**0.5)+1):
        if N // m == N % m:
            total += m
            if N // m != m:
                total += N // m
    return total

N = int(input())
print(find_sum_of_favorite_numbers(N))