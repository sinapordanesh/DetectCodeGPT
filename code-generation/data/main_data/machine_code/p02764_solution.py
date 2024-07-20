import math

def time_to_grill(N, K, coords):
    def time_taken(x, y):
        times = []
        for i in range(N):
            dist = math.sqrt((x - coords[i][0])**2 + (y - coords[i][1])**2)
            times.append(coords[i][2] * dist)
        times.sort()
        return sum(times[:K])
    
    left, right = -1000, 1000
    for _ in range(80):
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if time_taken(m1, 0) < time_taken(m2, 0):
            right = m2
        else:
            left = m1
    return round(time_taken(left, 0), 6) if time_taken(left, 0) < time_taken(right, 0) else round(time_taken(right, 0), 6)

# Sample Input 1
N = 4
K = 3
coords = [[-1, 0, 3], [0, 0, 3], [1, 0, 2], [1, 1, 40]]
print(time_to_grill(N, K, coords))

# Sample Input 2
N = 10
K = 5
coords = [[-879, 981, 26], [890, -406, 81], [512, 859, 97], [362, -955, 25], [128, 553, 17], [-885, 763, 2], [449, 310, 57], [-656, -204, 11], [-270, 76, 40], [184, 170, 16]]
print(time_to_grill(N, K, coords))