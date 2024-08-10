def longest_even_string(S):
    i = 1
    while S[:len(S)-i//2] != S[len(S)-i//2:]:
        i += 2
    return len(S) - i//2

S = input()
print(longest_even_string(S))