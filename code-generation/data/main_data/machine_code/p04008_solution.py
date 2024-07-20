def teleporter_destinations(N, K, destinations):
    changed = 0
    for i in range(N):
        count = 0
        current = i+1
        while current != 1 and count <= K:
            current = destinations[current-1]
            count += 1
        if count == K and current == 1:
            continue
        else:
            changed += 1
    return changed

# Sample Input 1
# N = 3
# K = 1
# destinations = [2, 3, 1]
# print(teleporter_destinations(N, K, destinations))

# Sample Input 2
# N = 4
# K = 2
# destinations = [1, 1, 2, 2]
# print(teleporter_destinations(N, K, destinations))

# Sample Input 3
# N = 8
# K = 2
# destinations = [4, 1, 2, 3, 1, 2, 3, 4]
# print(teleporter_destinations(N, K, destinations))