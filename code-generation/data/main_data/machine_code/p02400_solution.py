import math

def circle_area_circumference(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    print(f"{area} {circumference}")

# Test the function with sample inputs
circle_area_circumference(2)
circle_area_circumference(3)