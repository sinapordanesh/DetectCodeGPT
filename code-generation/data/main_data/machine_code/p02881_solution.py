def min_moves_to_reach_N(N):
    x = 1
    count = 0
    while x < N:
        x *= 2
        count += 1
    if x == N:
        return count
    return count + 1 if N % x > 0 else count

N = int(input())
print(min_moves_to_reach_N(N))