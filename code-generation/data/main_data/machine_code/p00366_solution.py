def electric_metronome(N, intervals):
    max_interval = max(intervals)
    total = sum(intervals)
    result = max(N * max_interval - total, 0)
    return result

# Sample Input 1
print(electric_metronome(3, [3, 6, 8])) # Output: 3

# Sample Input 2
print(electric_metronome(2, [10, 10])) # Output: 0