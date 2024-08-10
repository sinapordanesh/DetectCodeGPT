import math

def lowest_floor_to_crack_ball(velocity):
    time_to_reach_velocity = velocity / 9.8
    height = 4.9 * time_to_reach_velocity ** 2
    floor = math.ceil((height + 5) / 5)
    return floor

while True:
    try:
        velocity = float(input())
        print(lowest_floor_to_crack_ball(velocity))
    except EOFError:
        break