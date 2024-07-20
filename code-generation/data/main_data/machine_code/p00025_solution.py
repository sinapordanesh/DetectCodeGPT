import sys

def calculate_hit_and_blow(a, b):
    hit = 0
    blow = 0
    
    for i in range(4):
        if a[i] == b[i]:
            hit += 1
        elif a[i] in b:
            blow += 1
            
    return hit, blow

for line in sys.stdin:
    data = list(map(int, line.split()))
    a = data[:4]
    b = data[4:]
    
    hit, blow = calculate_hit_and_blow(a, b)
    print(hit, blow)