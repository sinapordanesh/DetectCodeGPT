import math

def distance_between_hands(A, B, H, M):
    hour_angle = 30 * H + 0.5 * M
    minute_angle = 6 * M
    
    angle_diff = abs(hour_angle - minute_angle)
    angle_diff = min(360 - angle_diff, angle_diff)
    
    distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle_diff)))
    
    return distance

A, B, H, M = map(int, input().split())
print(distance_between_hands(A, B, H, M))