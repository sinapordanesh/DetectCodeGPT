def max_num_of_robots(N, robots):
    robots.sort(key=lambda x: x[0])
    end = robots[0][0] - robots[0][1]
    count = 0
    
    for i in range(N):
        if robots[i][0] - robots[i][1] >= end:
            count += 1
            end = robots[i][0] + robots[i][1]
    
    return count

# Sample Input 1
N = 4
robots = [(2, 4), (4, 3), (9, 3), (100, 5)]
print(max_num_of_robots(N, robots))

# Sample Input 2
N = 2
robots = [(8, 20), (1, 10)]
print(max_num_of_robots(N, robots))

# Sample Input 3
N = 5
robots = [(10, 1), (2, 1), (4, 1), (6, 1), (8, 1)]
print(max_num_of_robots(N, robots))