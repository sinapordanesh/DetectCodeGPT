def dice_room_rotations(input_data):
    rotations = []
    for i in range(0, len(input_data), 6):
        dice = input_data[i:i+6]
        holes = [0, 0, 0, 0]
        for j in range(6):
            holes[j%4] += dice[j].count('*')
        min_rotations = min(holes[0], holes[1], holes[2], holes[3])
        rotations.append(min_rotations)
    return rotations

input_data = ['...', '...', '.*.', '...', '...', '.*.', '...', '...', '...', '...', '...', '.*.', '...', '...', '.*.', '...', '...', '...', '...', '.*.', '...', '.*.', '...', '*..', '...', '..*', '*.*', '*.*', '*.*', '*.*', '.*.', '*.*', '*..', '.*.', '..*', '*.*', '...', '*..', '...', '...', '.*.', '.*.', '...', '.**', '*..', '...', '...', '.*.', '.*.', '...', '*..', '..*', '...', '.**', '...', '*..', '...']
print(dice_room_rotations(input_data))