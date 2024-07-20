def max_flag_distance(N, flags):
    flags.sort(key=lambda x: x[0])
    ans = 0
    for i in range(1, N):
        ans = max(ans, flags[i][0] - flags[i-1][0])
    return ans

# Sample Input 1
N = 3
flags = [(1, 3), (2, 5), (1, 9)]
print(max_flag_distance(N, flags))

# Sample Input 2
N = 5
flags = [(2, 2), (2, 2), (2, 2), (2, 2), (2, 2)]
print(max_flag_distance(N, flags))

# Sample Input 3
N = 22
flags = [(93, 6440), (78, 6647), (862, 11), (8306, 9689), (798, 99), (801, 521), (188, 206), (6079, 971), (4559, 209), (50, 94), (92, 6270), (5403, 560), (803, 83), (1855, 99), (42, 504), (75, 484), (629, 11), (92, 122), (3359, 37), (28, 16), (648, 14), (11, 269)]
print(max_flag_distance(N, flags))