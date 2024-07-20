import math

def max_tilt_angle():
    a, b, x = map(int, input().split())
    if x >= (a*a*b)/2:
        tan_theta = (2*x)/(a*a*a - 2*b*x)
        theta = math.degrees(math.atan(tan_theta))
    else:
        tan_theta = (a*b*b)/(2*x)
        theta = math.degrees(math.atan(tan_theta))
    
    print('{:.10f}'.format(theta))

max_tilt_angle()