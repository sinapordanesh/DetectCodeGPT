def shift_string(N, S):
    result = ""
    for char in S:
        if char.isalpha():
            shift = (ord(char) - ord('A') + N) % 26
            result += chr(ord('A') + shift)
        else:
            result += char
    print(result)

# Input
N, S = map(int, input().split())

# Function Call
shift_string(N, S)