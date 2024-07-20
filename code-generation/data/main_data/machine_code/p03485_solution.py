import math

def average_rounded_up(a, b):
    x = (a + b) / 2
    return math.ceil(x) 

# Test the function
print(average_rounded_up(1, 3))
print(average_rounded_up(7, 4))
print(average_rounded_up(5, 5))