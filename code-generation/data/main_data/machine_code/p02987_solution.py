def check_two_chars(S):
    freq = {}
    for char in S:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    if len(freq) == 2 and freq[S[0]] == 2:
        print("Yes")
    else:
        print("No")

# Test cases
check_two_chars("ASSA")
check_two_chars("STOP")
check_two_chars("FFEE")
check_two_chars("FREE")