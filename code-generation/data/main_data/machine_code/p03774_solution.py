def nearest_checkpoint(N, M, student_coordinates, checkpoint_coordinates):
    for student in student_coordinates:
        min_dist = float('inf')
        min_idx = 0
        for idx, checkpoint in enumerate(checkpoint_coordinates):
            dist = abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1])
            if dist < min_dist:
                min_dist = dist
                min_idx = idx + 1
        print(min_idx)

# Sample Input 1
nearest_checkpoint(2, 2, [(2, 0), (0, 0)], [(-1, 0), (1, 0)])

# Sample Input 2
nearest_checkpoint(3, 4, [(10, 10), (-10, -10), (3, 3)], [(1, 2), (2, 3), (3, 5), (3, 5)])

# Sample Input 3
nearest_checkpoint(5, 5, [(-100000000, -100000000), (-100000000, 100000000), (100000000, -100000000), (100000000, 100000000), (0, 0)], [(0, 0), (100000000, 100000000), (100000000, -100000000), (-100000000, 100000000), (-100000000, -100000000)])