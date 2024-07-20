def number_of_integers_with_property(N, A):
    count = 0
    for i in range(N):
        has_property = True
        for j in range(N):
            if i != j and A[j] % A[i] == 0:
                has_property = False
                break
        if has_property:
            count += 1
    return count

N = 5
A = [24, 11, 8, 3, 16]
print(number_of_integers_with_property(N, A))

N = 4
A = [5, 5, 5, 5]
print(number_of_integers_with_property(N, A))

N = 10
A = [33, 18, 45, 28, 8, 19, 89, 86, 2, 4]
print(number_of_integers_with_property(N, A))