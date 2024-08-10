def calculate_table():
    r, c = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(r)]
    
    for row in table:
        row.append(sum(row))
    
    column_sums = [sum(col) for col in zip(*table)]
    table.append(column_sums)
    
    for row in table:
        print(*row)

calculate_table()