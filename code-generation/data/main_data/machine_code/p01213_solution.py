def longest_repeated_subsequence(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                for k in range(j+1, len(s)):
                    if s[k] == s[i]:
                        return s[i:k+1]

while True:
    s = input()
    if s == "#END":
        break
    print(longest_repeated_subsequence(s))