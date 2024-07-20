def max_duration(n, p, q, channels):
    if n == 0:
        return 0
    start_time = p
    end_time = q
    max_duration = 0
    for i in range(n):
        for j in range(i+1, n):
            duration = channels[i][0]
            for c1, c2 in zip(channels[i][1:], channels[j][1:]):
                if c1 < start_time < c2:
                    duration += c2 - start_time
                elif c1 > end_time:
                    duration += end_time - start_time
                    break
            else:
                duration += end_time - max(c2, start_time)
            max_duration = max(max_duration, duration)
    return max_duration

# Sample Input
print(max_duration(1, 2100, 2400, [(1, 2130, 2200)])) # Output: 120
print(max_duration(3, 2100, 2400, [(3, 2100, 2130, 2200, 2230, 2300, 2330), (2, 2130, 2200, 2330, 2400), (2, 2100, 2130, 2330, 2400)])) # Output: 180