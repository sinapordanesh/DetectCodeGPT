def blue_balls_in_row(N, A, B):
    blue_balls = (N // (A + B)) * A
    remaining = N % (A + B)
    if remaining >= A:
        blue_balls += A
    else:
        blue_balls += remaining
    return blue_balls

# Sample Input 1
print(blue_balls_in_row(8, 3, 4))

# Sample Input 2
print(blue_balls_in_row(8, 0, 4))

# Sample Input 3
print(blue_balls_in_row(6, 2, 4))