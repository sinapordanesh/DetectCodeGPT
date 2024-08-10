from math import cos, sin, pi

def expected_center(N, L, T):
    x_sum = 0
    y_sum = 0
    
    for i in range(N):
        x_sum += cos(2*pi*T[i]/L)
        y_sum += sin(2*pi*T[i]/L)
    
    x_center = x_sum/N
    y_center = y_sum/N
    
    return x_center, y_center

# Input
N, L = map(int, input().split())
T = [int(input()) for _ in range(N)]

# Output
x_center, y_center = expected_center(N, L, T)
print(f"{x_center:.15f} {y_center:.15f}")