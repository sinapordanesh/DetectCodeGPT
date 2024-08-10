def shortest_path(sx, sy, tx, ty):
    path = ""
    path += "U" * (ty - sy)
    path += "R" * (tx - sx)
    path += "D" * (ty - sy)
    path += "L" * (tx - sx)
    path += "L"
    path += "U" * (ty - sy + 1)
    path += "R" * (tx - sx + 1)
    path += "D"
    path += "R"
    path += "U" * (ty - sy + 1)
    path += "L" * (tx - sx + 1)
    
    return path

# Sample Input 1
print(shortest_path(0, 0, 1, 2))

# Sample Input 2
print(shortest_path(-2, -2, 1, 1))