def holding_buttons_time(A, B, C, D):
    start_time = max(A, C)
    end_time = min(B, D)
    
    return max(0, end_time - start_time)

# Read input values
A, B, C, D = map(int, input().split())

# Calculate and print the duration of holding both buttons down
print(holding_buttons_time(A, B, C, D))