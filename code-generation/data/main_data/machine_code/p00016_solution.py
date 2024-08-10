import math

def treasure_hunt():
    x = 0
    y = 0
    
    while True:
        d, t = map(int, input().split(','))
        if d == 0 and t == 0:
            break
            
        x += d * math.cos(math.radians(t))
        y += d * math.sin(math.radians(t))
    
    print(int(x))
    print(int(y))

treasure_hunt()