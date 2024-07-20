def ramen_price(S):
    price = 700
    for char in S:
        if char == 'o':
            price += 100
    return price

# Test the function with sample inputs
print(ramen_price("oxo"))
print(ramen_price("ooo"))
print(ramen_price("xxx"))