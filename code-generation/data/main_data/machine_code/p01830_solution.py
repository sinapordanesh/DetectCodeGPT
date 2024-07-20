def delete_files(N, files):
    count = 0
    for i in range(N):
        if files[i][0] == 'y':
            count += 1
    return count

# Sample Input 1
N = 3
files = [['y', 7], ['y', 6], ['n', 5]]
print(delete_files(N, files))

# Sample Input 2
N = 3
files = [['y', 7], ['n', 6], ['y', 5]]
print(delete_files(N, files))

# Sample Input 3
N = 6
files = [['y', 4], ['n', 5], ['y', 4], ['y', 6], ['n', 3], ['y', 6]]
print(delete_files(N, files))