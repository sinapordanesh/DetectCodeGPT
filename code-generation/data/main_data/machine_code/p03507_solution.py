def find_flower_position(N, K, flowers):
    position = 0
    for w, d in flowers:
        position = max(position, w + d * (K - 1))
    return position