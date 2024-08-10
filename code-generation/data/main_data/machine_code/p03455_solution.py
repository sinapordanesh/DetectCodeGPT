def determine_product_odd_or_even():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")

determine_product_odd_or_even()