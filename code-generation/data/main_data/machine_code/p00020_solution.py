def capitalize_text(text):
    converted_text = ""
    for char in text:
        if char.islower():
            converted_text += char.upper()
        else:
            converted_text += char
    print(converted_text)

# Sample Input
capitalize_text("this is a pen.")