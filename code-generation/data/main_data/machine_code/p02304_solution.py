def find_intersection(n, segments):
    vertical_lines = []
    horizontal_lines = []
    vertical_count = 0
    horizontal_count = 0
    for segment in segments:
        if segment[0] == segment[2]:
            vertical_lines.append(segment)
        else:
            horizontal_lines.append(segment)

    for i in range(len(vertical_lines)):
        for j in range(i+1, len(vertical_lines)):
            if vertical_lines[i][1] <= vertical_lines[j][1] <= vertical_lines[i][3] or vertical_lines[i][3] <= vertical_lines[j][1] <= vertical_lines[i][1]:
                vertical_count += 1

    for i in range(len(horizontal_lines)):
        for j in range(i+1, len(horizontal_lines)):
            if horizontal_lines[i][0] <= horizontal_lines[j][0] <= horizontal_lines[i][2] or horizontal_lines[i][2] <= horizontal_lines[j][0] <= horizontal_lines[i][0]:
                horizontal_count += 1

    return vertical_count + horizontal_count

n = 6
segments = [(2, 2, 2, 5), (1, 3, 5, 3), (4, 1, 4, 4), (5, 2, 7, 2), (6, 1, 6, 3), (6, 5, 6, 7)]
print(find_intersection(n, segments))