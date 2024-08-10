def lexicographically_largest_string(N, S):
    cnt_a = N
    cnt_b = N
    result = ""
    for char in S:
        if char == "a":
            if cnt_b > 0:
                result += char
                cnt_b -= 1
        else:
            if cnt_a > 0:
                result += char
                cnt_a -= 1
    return result

N = int(input())
S = input()
print(lexicographically_largest_string(N, S))