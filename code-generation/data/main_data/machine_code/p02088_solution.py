def union_ball(N, balls):
    even_count = 0
    for ball in balls:
        if ball % 2 == 0:
            even_count += 1
    
    if even_count == 0 or even_count == N:
        return 0
    else:
        return (N - 1) // 2

# Sample Input
N = 3
balls = [4, 5, 6]
print(union_ball(N, balls))

N = 4
balls = [4, 2, 4, 2]
print(union_ball(N, balls))