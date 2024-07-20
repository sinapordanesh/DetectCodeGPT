def min_operations_to_palindrome(s):
    n = len(s)
    cnt = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            cnt += 1
    return cnt

s = input().strip()
result = min_operations_to_palindrome(s)
if result == 0:
    print(0)
elif result == 1:
    print(1)
else:
    print(result)