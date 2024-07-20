def determine_winner(N, areas):
    total_black = 0
    total_white = 0
    for area in areas:
        total_white += area[0]
        total_black += area[1]
    
    if total_white % 2 == 0:
        return 1
    else:
        return 0

# Sample Input 1
N = 4
areas = [(24, 99), (15, 68), (12, 90), (95, 79)]
print(determine_winner(N, areas))

# Sample Input 2
N = 3
areas = [(2, 46), (94, 8), (46, 57)]
print(determine_winner(N, areas))