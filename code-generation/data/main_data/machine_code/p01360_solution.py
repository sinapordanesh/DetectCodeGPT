def calculate_footstep_violations(input_data):
    output = []
    for data in input_data:
        count = 0
        left_foot = False
        right_foot = False
        for i in range(len(data) - 1):
            if data[i] != data[i + 1]:
                if (data[i] % 3 == 0 and data[i + 1] == data[i] - 1) or \
                   (data[i] % 3 == 1 and data[i + 1] == data[i] + 1):
                    continue
                if left_foot and data[i + 1] % 3 == 0:
                    count += 1
                    left_foot = False
                elif right_foot and data[i + 1] % 3 == 1:
                    count += 1
                    right_foot = False
            else:
                if data[i] % 3 == 0:
                    left_foot = True
                elif data[i] % 3 == 1:
                    right_foot = True
        output.append(count)
    return output

input_data = ["1", "12", "123", "369", "6748", "4247219123", "1232123212321232"]
print(calculate_footstep_violations(input_data))