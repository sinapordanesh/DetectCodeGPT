def count_sequences_less_than(s):
    n = len(s)
    result = 0
    for i in range(10**n):
        seq = str(i).zfill(n)
        if seq < s:
            result += 1
    return result

# Read input
s = input().strip()

# Call the function and print the result
print(count_sequences_less_than(s))