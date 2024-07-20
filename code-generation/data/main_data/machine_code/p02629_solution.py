def dog_name(N):
    result = ""
    while N > 0:
        N -= 1
        result = chr(97 + N % 26) + result
        N //= 26
    return result

N = int(input())
print(dog_name(N))