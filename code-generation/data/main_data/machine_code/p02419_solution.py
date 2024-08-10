def find_word_count():
    word = input().lower()
    text = ""
    while True:
        line = input()
        if line == "END_OF_TEXT":
            break
        text += line.lower() + " "
    
    words = text.split()
    count = words.count(word)
    print(count)

find_word_count()