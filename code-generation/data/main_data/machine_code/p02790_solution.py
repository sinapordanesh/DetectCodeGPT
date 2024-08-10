def lexicographically_smaller(a, b):
    str1 = str(a) * b
    str2 = str(b) * a
    if str1 < str2:
        return str1
    else:
        return str2

# Sample Input 1
print(lexicographically_smaller(4, 3))

# Sample Input 2
print(lexicographically_smaller(7, 7))