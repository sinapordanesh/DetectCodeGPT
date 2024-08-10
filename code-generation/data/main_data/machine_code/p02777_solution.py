def balls_after_throwaway(S, T, A, B, U):
    if U == S:
        return A-1, B
    else:
        return A, B-1

# Sample Input 1
print(balls_after_throwaway("red", "blue", 3, 4, "red")) # Output: 2 4

# Sample Input 2
print(balls_after_throwaway("red", "blue", 5, 5, "blue")) # Output: 5 4