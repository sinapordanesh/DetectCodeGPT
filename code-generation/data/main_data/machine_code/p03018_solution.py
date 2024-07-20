def max_operations(s):
    count = 0
    while 'ABC' in s:
        s = s.replace('ABC', 'BCA')
        count += 1
    return count

# Test the function
print(max_operations("ABCABC"))
print(max_operations("C"))
print(max_operations("ABCACCBABCBCAABCB"))