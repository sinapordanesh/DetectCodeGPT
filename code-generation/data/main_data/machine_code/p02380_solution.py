import math

def triangle_properties(a, b, C):
    S = 0.5 * a * b * math.sin(math.radians(C))
    L = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))
    h = b * math.sin(math.radians(C))
    
    print("{:.8f}".format(S))
    print("{:.8f}".format(L))
    print("{:.8f}".format(h))

# Sample input
triangle_properties(4, 3, 90)