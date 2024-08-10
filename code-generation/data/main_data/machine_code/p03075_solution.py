def antennas_communication(a, b, c, d, e, k):
    if d - a > k:
        return ":("
    elif e - b > k:
        return ":("
    elif e - c > k:
        return ":("
    else:
        return "Yay!"