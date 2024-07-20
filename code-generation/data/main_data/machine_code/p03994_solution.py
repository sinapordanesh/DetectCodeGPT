def smallest_lexicographically_string(s, K):
    for i in range(len(s)):
        if K == 0:
            break
        if s[i] != 'a':
            diff = ord('z') - ord(s[i]) + 1
            if diff <= K:
                s = s[:i] + 'a' + s[i+1:]
                K -= diff
    if K > 0:
        s = s[:-1] + chr((ord(s[-1]) - ord('a') + K) % 26 + ord('a'))
    return s

# Sample Input 1
print(smallest_lexicographically_string('xyz', 4))

# Sample Input 2
print(smallest_lexicographically_string('a', 25))

# Sample Input 3
print(smallest_lexicographically_string('codefestival', 100))