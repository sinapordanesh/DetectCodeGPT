import sys

def minimal_length_water_pipes(N, M, data):
    total_length = 0
    stop_valves = set()
    
    for i in range(N):
        x_si, y_si, x_di, y_di = data[i]
        total_length += abs(x_si - x_di) + abs(y_si - y_di)
    
    for i in range(N, N+M):
        x_vi, y_vi = data[i]
        stop_valves.add((x_vi, y_vi))
    
    x_b, y_b = data[N+M]
    x_c, y_c = data[N+M+1]
    
    if (x_c, y_c) == (x_b, y_b):
        print(total_length)
    else:
        min_length = float('inf')
        for i in range(N):
            x_si, y_si, x_di, y_di = data[i]
            if (x_si, y_si) in stop_valves and (x_di, y_di) in stop_valves:
                continue
            if (x_si, y_si) == (x_b, y_b) or (x_di, y_di) == (x_b, y_b):
                min_length = min(min_length, total_length - (abs(x_si - x_di) + abs(y_si - y_di)))
        
        if min_length == float('inf'):
            print(-1)
        else:
            print(min_length)

input_lines = sys.stdin.readlines()
N, M = map(int, input_lines[0].split())
data = [list(map(int, line.split())) for line in input_lines[1:]]

minimal_length_water_pipes(N, M, data)