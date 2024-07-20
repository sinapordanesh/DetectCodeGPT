def children_on_squares(s):
    n = len(s)
    count = [0] * n
    for i in range(n):
        if s[i] == 'R':
            j = i
            while s[j] == 'R':
                j += 1
            if (j - i) % 2 == 0:
                count[j] += 1
            else:
                count[j - 1] += 1
        else:
            j = i
            while s[j] == 'L':
                j -= 1
            if (i - j) % 2 == 0:
                count[j] += 1
            else:
                count[j + 1] += 1
    return ' '.join(map(str, count))

# Test the function with the sample inputs
print(children_on_squares("RRLRL"))
print(children_on_squares("RRLLLLRLRRLL"))
print(children_on_squares("RRRLLRLLRRRLLLLL"))