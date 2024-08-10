def maximize_count(N, a):
    max_value = max(a)
    count_max = a.count(max_value)
    count_min = a.count(max_value-1)
    
    if count_max >= count_min:
        return count_max
    else:
        return count_max + 1 if count_max % 2 == 0 else count_max

# Read input values
N = int(input())
a = list(map(int, input().split()))

# Call the function and print the output
print(maximize_count(N, a))