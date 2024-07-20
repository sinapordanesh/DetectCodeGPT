def count_box_combinations(R, G, B, N):
    count = 0
    for r in range(N//R + 1):
        for g in range(N//G + 1):
            num_balls = r*R + g*G
            if num_balls <= N:
                b = (N - num_balls) // B
                if num_balls + b*B == N:
                    count += 1
    return count

R, G, B, N = map(int, input().split())
print(count_box_combinations(R, G, B, N))