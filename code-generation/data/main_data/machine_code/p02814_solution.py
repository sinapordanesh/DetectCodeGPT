def semi_common_multiples(N, M, A):
    count = 0
    for i in range(1, M+1):
        is_semi_common_multiple = True
        for a in A:
            if (i % a != 0) and (i % (a//2) != 0):
                is_semi_common_multiple = False
                break
        if is_semi_common_multiple:
            count += 1
    return count

#Sample Input 1
print(semi_common_multiples(2, 50, [6, 10]))

#Sample Input 2
print(semi_common_multiples(3, 100, [14, 22, 40]))

#Sample Input 3
print(semi_common_multiples(5, 1000000000, [6, 6, 2, 6, 2]))