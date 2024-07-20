def is_concatenation_of_two_copies(N, S):
    if N % 2 == 0 and S[:N//2] == S[N//2:]:
        return "Yes"
    else:
        return "No"