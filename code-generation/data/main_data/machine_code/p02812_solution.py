def count_ABC_occurrences(N, S):
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    return count

# Sample Input 1
print(count_ABC_occurrences(10, "ZABCDBABCQ"))

# Sample Input 2
print(count_ABC_occurrences(19, "THREEONEFOURONEFIVE"))

# Sample Input 3
print(count_ABC_occurrences(33, "ABCCABCBABCCABACBCBBABCBCBCBCABCB"))