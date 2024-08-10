def dice_simulation():
    faces = list(map(int, input().split()))
    commands = input().strip()
    
    top = faces[0]
    north = faces[1]
    east = faces[2]
    west = faces[3]
    south = faces[4]
    bottom = faces[5]
    
    for command in commands:
        if command == 'N':
            top, north, bottom, south = south, top, north, bottom
        elif command == 'E':
            top, east, bottom, west = west, top, east, bottom
        elif command == 'S':
            top, south, bottom, north = north, top, south, bottom
        elif command == 'W':
            top, west, bottom, east = east, top, west, bottom
    
    print(top)

dice_simulation()