def good_pairs(N, strings):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if len(set(strings[i]) - set(strings[j])) == 0 or len(set(strings[j]) - set(strings[i])) == 0:
                count += 1
    return count

# Sample Input 1
N = 3
strings = ["abcxyx", "cyx", "abc"]
print(good_pairs(N, strings))

# Sample Input 2
N = 6
strings = ["b", "a", "abc", "c", "d", "ab"]
print(good_pairs(N, strings))