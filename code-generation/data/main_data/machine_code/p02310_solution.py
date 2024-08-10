import math

def tangent_to_circle(px, py, cx, cy, r):
    dist = math.sqrt((px - cx)**2 + (py - cy)**2)
    angle = math.atan2(py - cy, px - cx)
    angle1 = math.asin(r / dist)
    
    x1 = cx + r * math.cos(angle + angle1)
    y1 = cy + r * math.sin(angle + angle1)
    x2 = cx + r * math.cos(angle - angle1)
    y2 = cy + r * math.sin(angle - angle1)
    
    if x1 < x2 or (x1 == x2 and y1 < y2):
        return (x1, y1), (x2, y2)
    else:
        return (x2, y2), (x1, y1)