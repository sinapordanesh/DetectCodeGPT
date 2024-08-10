def shortest_spell(n, enemies):
    spell = ""
    while any(1 in row for row in enemies):
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        for i in range(n):
            if 1 in enemies[i]:
                start_row = i
                start_col = enemies[i].index(1)
                break
        for i in range(n-1, -1, -1):
            if 1 in enemies[i]:
                end_row = i
                end_col = enemies[i].index(1, start_col)
                break
        spell += "myon" * (abs(start_row - end_row) + 1) * (abs(start_col - end_col) + 1)
        for i in range(start_row, end_row+1):
            for j in range(start_col, end_col+1):
                enemies[i][j] = 0
    return spell

n = int(input())
while n != 0:
    enemies = []
    for _ in range(n):
        row = list(map(int, input().split()))
        enemies.append(row)
    print(shortest_spell(n, enemies))
    n = int(input())