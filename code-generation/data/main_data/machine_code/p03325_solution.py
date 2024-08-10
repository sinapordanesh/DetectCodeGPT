def max_operations(N, a):
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            count += 1
    return count

# Sample Input 1
# N = 3
# a = [5, 2, 4]
# Sample Output 1
# Expected Output: 3
print(max_operations(3, [5, 2, 4]))

# Sample Input 2
# N = 4
# a = [631, 577, 243, 199]
# Sample Output 2
# Expected Output: 0
print(max_operations(4, [631, 577, 243, 199]))

# Sample Input 3
# N = 10
# a = [2184, 2126, 1721, 1800, 1024, 2528, 3360, 1945, 1280, 1776]
# Sample Output 3
# Expected Output: 39
print(max_operations(10, [2184, 2126, 1721, 1800, 1024, 2528, 3360, 1945, 1280, 1776]))