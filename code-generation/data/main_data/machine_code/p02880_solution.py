def can_be_product_of_two_integers(N):
    for i in range(1, 10):
        if N % i == 0 and N // i <= 9:
            return "Yes"
    return "No"

N = int(input())
print(can_be_product_of_two_integers(N))