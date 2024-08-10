def max_i(s, t):
    if t in s * 2:
        return 1
    for i in range(1, len(s) + 1):
        if t in s * i:
            return i - 1
    return -1

# Test the function
print(max_i("abcabab", "ab"))
print(max_i("aa", "aaaaaaa"))
print(max_i("aba", "baaab"))