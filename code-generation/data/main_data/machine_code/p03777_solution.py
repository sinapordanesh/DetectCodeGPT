def honest_or_dishonest(a, b):
    if a == "H" and b == "H":
        return "H"
    elif a == "H" and b == "D":
        return "D"
    elif a == "D" and b == "H":
        return "D"
    else:
        return "H"