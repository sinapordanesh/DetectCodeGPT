def check_stability(input_data):
    w, h = map(int, input_data[0].split())
    building = []
    for i in range(1, h + 1):
        building.append(list(input_data[i]))

    for i in range(h):
        for j in range(w):
            if building[i][j] != '.':
                x_left = j
                while j < w and building[i][j] == building[i][x_left]:
                    j += 1
                x_right = j - 1

                x_sum = 0
                count = 0
                for k in range(i, h):
                    for l in range(x_left, x_right + 1):
                        if building[k][l] == building[i][x_left]:
                            x_sum += l + 0.5
                            count += 1

                center_of_mass = x_sum / count
                if not (x_left < center_of_mass < x_right):
                    return "UNSTABLE"
    
    return "STABLE"

# Read input data
input_data = []
while True:
    line = input()
    if line == "0 0":
        break
    input_data.append(line)

# Check stability for each dataset
for i in range(0, len(input_data), int(input_data[i].split()[1]) + 1):
    print(check_stability(input_data[i:i + int(input_data[i].split()[1]) + 1]))