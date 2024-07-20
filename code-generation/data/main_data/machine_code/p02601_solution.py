def magic_successful(red, green, blue, k):
    for i in range(k+1):
        if green > red and blue > green:
            return "Yes"
        if red >= green:
            green *= 2
        elif green >= blue:
            blue *= 2
        else:
            break
    return "No"

A, B, C, K = map(int, input().split())
print(magic_successful(A, B, C, K))