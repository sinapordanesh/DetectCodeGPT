def point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
    def sign(x1, y1, x2, y2, x3, y3):
        return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
    
    b1 = sign(xp, yp, x1, y1, x2, y2) < 0.0
    b2 = sign(xp, yp, x2, y2, x3, y3) < 0.0
    b3 = sign(xp, yp, x3, y3, x1, y1) < 0.0
    
    if ((b1 == b2) and (b2 == b3)):
        print("YES")
    else:
        print("NO")

# Read input and call function for each dataset
import sys
for line in sys.stdin:
    data = list(map(float, line.split()))
    point_in_triangle(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])