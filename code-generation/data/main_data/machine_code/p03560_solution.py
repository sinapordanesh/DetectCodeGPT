def smallest_sum_of_digits(K):
    if K % 9 == 0:
        return 9
    else:
        return K % 9

K = int(input())
print(smallest_sum_of_digits(K))