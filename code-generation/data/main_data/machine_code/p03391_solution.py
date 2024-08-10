def candies_given_to_Takahashi(N, A, B):
    candies = 0
    while A != B:
        max_diff = 0
        max_diff_index = -1
        for i in range(N):
            diff = A[i] - B[i]
            if diff > max_diff:
                max_diff = diff
                max_diff_index = i
        if max_diff_index == -1:
            break
        A[max_diff_index] -= 1
        B[max_diff_index] += 1
        candies += 1
    return candies

# Sample Input 1
N = 2
A = [1, 2]
B = [3, 2]
print(candies_given_to_Takahashi(N, A, B))

# Sample Input 2
N = 3
A = [8, 3, 4]
B = [0, 1, 8]
print(candies_given_to_Takahashi(N, A, B))

# Sample Input 3
N = 1
A = [1]
B = [1]
print(candies_given_to_Takahashi(N, A, B))