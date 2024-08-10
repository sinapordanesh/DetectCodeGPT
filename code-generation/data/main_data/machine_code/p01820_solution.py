import math

def calculate_max_speed(n, points):
    speed = 1
    for point in points:
        if point[2] == '>':
            speed *= 2
        elif point[2] == '<':
            speed *= 2
        elif point[2] == 'v':
            speed *= 2
        elif point[2] == '^':
            speed *= 2
    
    return int(math.log2(speed))

# Sample Input
print(calculate_max_speed(9, [(0, 0, 'v'), (1, 0, '>'), (2, 0, '<'), (0, 1, '>'), (1, 1, 'v'), (2, 1, 'v'), (0, 2, '^'), (1, 2, '^'), (2, 2, '<')]))
print(calculate_max_speed(9, [(0, 0, '^'), (1, 0, '^'), (2, 0, '^'), (0, 1, '<'), (1, 1, '^'), (2, 1, '>'), (0, 2, 'v'), (1, 2, 'v'), (2, 2, 'v')]))