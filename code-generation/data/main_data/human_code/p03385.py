def atc_093a(input_value):
    try:
        input_value.index("a")
        input_value.index("b")
        input_value.index("c")
        return "Yes"
    except ValueError:
        return "No"

input_value = input()
print(atc_093a(input_value))