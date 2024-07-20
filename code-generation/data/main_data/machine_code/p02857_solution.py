def interactive_task():
    N = int(input())
    
    def query_balls(balls):
        print("?", *balls)
        return input()
    
    def guess_colors(colors):
        print("!", colors)
    
    red_count = 0
    blue_count = 0
    colors = []
    
    for i in range(1, 2*N+1, 2):
        query_result = query_balls([i, i+1, i+2])
        
        if query_result == "Red":
            red_count += 2
            colors.extend(['R', 'R'])
        elif query_result == "Blue":
            blue_count += 2
            colors.extend(['B', 'B'])
    
    for i in range(2, 2*N, 4):
        query_result = query_balls([i, i+1, i+3])
        
        if query_result == "Red":
            red_count += 1
            colors.append('R')
        elif query_result == "Blue":
            blue_count += 1
            colors.append('B')
    
    remaining_red = N - red_count
    remaining_blue = N - blue_count
    
    for i in range(1, 2*N+1):
        if colors[i-1] == 'R':
            if remaining_red > 0:
                remaining_red -= 1
            else:
                colors[i-1] = 'B'
        elif colors[i-1] == 'B':
            if remaining_blue > 0:
                remaining_blue -= 1
            else:
                colors[i-1] = 'R'
    
    guess_colors(''.join(colors))

interactive_task()