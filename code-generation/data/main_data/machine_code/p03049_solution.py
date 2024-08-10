def max_occurrences_of_AB(N, strings):
    ab_count = 0
    for string in strings:
        ab_count += string.count("AB")
    return ab_count

# Sample Input 1
N = 3
strings = ["ABCA", "XBAZ", "BAD"]
print(max_occurrences_of_AB(N, strings))

# Sample Input 2
N = 9
strings = ["BEWPVCRWH", "ZZNQYIJX", "BAVREA", "PA", "HJMYITEOX", "BCJHMRMNK", "BP", "QVFABZ", "PRGKSPUNA"]
print(max_occurrences_of_AB(N, strings))

# Sample Input 3
N = 7
strings = ["RABYBBE", "JOZ", "BMHQUVA", "BPA", "ISU", "MCMABAOBHZ", "SZMEHMA"]
print(max_occurrences_of_AB(N, strings))