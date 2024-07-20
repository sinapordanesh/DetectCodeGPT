import math

def max_circle_radius():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    max_radius = 2 * area / (a + b + c)
    
    print(max_radius)

max_circle_radius()