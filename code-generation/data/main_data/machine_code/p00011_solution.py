def amidakuji(w, n, lines):
    vertical_lines = list(range(1, w+1))
    
    for line in lines:
        a, b = line.split(',')
        a, b = int(a), int(b)
        vertical_lines[a-1], vertical_lines[b-1] = vertical_lines[b-1], vertical_lines[a-1]
    
    return vertical_lines

print(amidakuji(5, 4, ["2,4", "3,5", "1,2", "3,4"]))