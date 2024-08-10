import math

def circumference_of_circle(R):
    return 2 * math.pi * R

R = int(input())
print("{:.20f}".format(circumference_of_circle(R)))