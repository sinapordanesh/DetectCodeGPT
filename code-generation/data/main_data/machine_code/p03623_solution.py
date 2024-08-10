def closer_store(x, a, b):
    if abs(x - a) < abs(x - b):
        return "A"
    else:
        return "B"