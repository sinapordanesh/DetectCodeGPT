import sys

def find_max_area(W, H, x, y):
    area1 = max(x * H, (W - x) * H)
    area2 = max(y * W, (H - y) * W)
    
    max_area = max(area1, area2)
    
    count = 0
    if area1 == max_area:
        count += 1
    if area2 == max_area:
        count += 1
    
    print("{:.6f} {}".format(max_area, count))

input_values = sys.stdin.readline().strip().split()
W = int(input_values[0])
H = int(input_values[1])
x = int(input_values[2])
y = int(input_values[3])

find_max_area(W, H, x, y)