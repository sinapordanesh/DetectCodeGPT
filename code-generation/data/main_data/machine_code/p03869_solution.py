import math

def maximum_circle_radius():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    
    s = (a + b + c) / 2
    
    radius = 2 * math.sqrt(s * (s - a) * (s - b) * (s - c)) / (a + b + c)
    
    print(radius)

maximum_circle_radius()