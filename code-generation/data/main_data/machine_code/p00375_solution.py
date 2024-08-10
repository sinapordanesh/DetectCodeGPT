def convert_fahrenheit_to_celsius(F):
    C = (F - 30) // 2
    return C

F = int(input())
print(convert_fahrenheit_to_celsius(F))