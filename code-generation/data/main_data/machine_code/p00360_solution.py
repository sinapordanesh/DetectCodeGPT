def swap_chars(s, k):
    s = list(s)
    n = len(s)
    i = 0
    while k > 0 and i < n - 1:
        if s[i] > s[i+1]:
            j = i
            while j > 0 and s[j-1] > s[j+1]:
                j -= 1
            s[j], s[j+1] = s[j+1], s[j]
            k -= (i - j)
            i = j
        i += 1
    return ''.join(s)

# Sample Input 1
# s = "pckoshien"
# k = 3
# print(swap_chars(s, k))

# Sample Input 2
# s = "pckoshien"
# k = 10
# print(swap_chars(s, k))