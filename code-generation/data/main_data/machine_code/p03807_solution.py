def possible_to_have_one_integer(N, A):
    count_odd = 0
    for num in A:
        if num % 2 != 0:
            count_odd += 1
    if count_odd % 2 == 0 or count_odd == 1:
        return "YES"
    else:
        return "NO" 

# Sample Input 1
print(possible_to_have_one_integer(3, [1, 2, 3]))

# Sample Input 2
print(possible_to_have_one_integer(5, [1, 2, 3, 4, 5]))