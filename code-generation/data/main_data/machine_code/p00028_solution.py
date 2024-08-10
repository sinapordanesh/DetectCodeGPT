from collections import Counter

def mode_value(sequence):
    count = Counter(sequence)
    max_freq = max(count.values())
    mode_values = [key for key, value in count.items() if value == max_freq]
    mode_values.sort()
    for value in mode_values:
        print(value)

# Read input from user
n = int(input())
sequence = []
for _ in range(n):
    num = int(input())
    sequence.append(num)

mode_value(sequence)