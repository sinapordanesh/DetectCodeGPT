def slimming_plan(S, T, D, weights):
    current_weight = S
    days = 0
    while current_weight > T and days < 100000:
        current_weight += weights[days % D]
        days += 1
        if current_weight <= T:
            return days
    return -1