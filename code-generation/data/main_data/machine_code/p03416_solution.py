def count_palindromic_numbers(A, B):
    count = 0
    for num in range(A, B+1):
        if str(num) == str(num)[::-1]:
            count += 1
    return count

A, B = map(int, input().split())
print(count_palindromic_numbers(A, B))