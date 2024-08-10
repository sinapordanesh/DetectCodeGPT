def bicube(H, W, sheet):
    def check_colorful(color):
        for row in sheet:
            for char in row:
                if char.isalpha() and char.lower() == color:
                    return True
        return False

    colors = set()
    for row in sheet:
        for char in row:
            if char.isalpha():
                colors.add(char.lower())

    if len(colors) != 8:
        return "No"

    for color in colors:
        if not check_colorful(color):
            return "No"

    return "Yes"