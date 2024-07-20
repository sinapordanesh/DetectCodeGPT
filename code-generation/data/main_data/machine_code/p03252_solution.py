def can_be_made_equal(S, T):
    if sorted(S) != sorted(T):
        return "No"
    return "Yes" 

S, T = input().split()
print(can_be_made_equal(S, T))