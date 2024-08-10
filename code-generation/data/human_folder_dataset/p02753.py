
def atc_158a(input_value: str) -> str:
    if input_value == "AAA" or input_value == "BBB":
        return "No"
    return "Yes"


input_value = input()
print(atc_158a(input_value))