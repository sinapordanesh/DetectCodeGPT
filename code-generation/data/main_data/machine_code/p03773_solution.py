def contest_start_time(A, B):
    start_time = (A + B) % 24
    return start_time

# Test the function with the sample inputs
print(contest_start_time(9, 12))
print(contest_start_time(19, 0))
print(contest_start_time(23, 2))