def median_values(N, values):
    medians = set()
    for value in values:
        medians.add(value[0])
        medians.add((value[0] + value[1]) / 2)
        medians.add(value[1])
    return len(medians)