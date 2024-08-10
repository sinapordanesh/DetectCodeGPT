def count_characters(sentence):
    counts = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in counts:
            print(char, ':', counts[char])
        else:
            print(char, ':', 0)