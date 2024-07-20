def product_sign(a, b):
    product = 1
    for i in range(a, b+1):
        product *= i
    if product > 0:
        print("Positive")
    elif product < 0:
        print("Negative")
    else:
        print("Zero")