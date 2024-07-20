def toggle_cases(input_str):
    result = ""
    for char in input_str:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

# Sample Input
input_str = "fAIR, LATER, OCCASIONALLY CLOUDY."
print(toggle_cases(input_str))