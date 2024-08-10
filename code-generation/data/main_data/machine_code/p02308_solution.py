import math

def cross_points_circle_line():
    cx, cy, r = map(int, input().split())
    q = int(input())
    
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        
        dx = x2 - x1
        dy = y2 - y1
        A = dx**2 + dy**2
        B = 2*dx*(x1 - cx) + 2*dy*(y1 - cy)
        C = (x1 - cx)**2 + (y1 - cy)**2 - r**2
        
        t = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
        
        x = x1 + t*dx
        y = y1 + t*dy
        
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        
        if (x1 <= x <= x2 and y1 <= y <= y2):
            print("{:.8f} {:.8f} {:.8f} {:.8f}".format(x, y, x, y))
        else:
            t = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)
            
            x = x1 + t*dx
            y = y1 + t*dy
            
            print("{:.8f} {:.8f} {:.8f} {:.8f}".format(x, y, x, y))

cross_points_circle_line()