def minimum_recorders(N, C, programs):
    channels = [0] * (10**5 + 1)
    for program in programs:
        s, t, c = program
        for i in range(s*2 - 1, t*2):
            channels[i] += 1

    return max(channels)

# Sample Input 1
N = 3
C = 2
programs = [(1, 7, 2), (7, 8, 1), (8, 12, 1)]
print(minimum_recorders(N, C, programs))

# Sample Input 2
N = 3
C = 4
programs = [(1, 3, 2), (3, 4, 4), (1, 4, 3)]
print(minimum_recorders(N, C, programs))

# Sample Input 3
N = 9
C = 4
programs = [(56, 60, 4), (33, 37, 2), (89, 90, 3), (32, 43, 1), (67, 68, 3), (49, 51, 3), (31, 32, 3), (70, 71, 1), (11, 12, 3)]
print(minimum_recorders(N, C, programs))