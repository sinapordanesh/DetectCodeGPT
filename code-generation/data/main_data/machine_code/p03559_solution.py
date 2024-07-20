def build_altars(N, upper_parts, middle_parts, lower_parts):
    count = 0
    for i in range(N):
        count += len(set([upper_parts[i], middle_parts[i], lower_parts[i]]))
    return count * count * count