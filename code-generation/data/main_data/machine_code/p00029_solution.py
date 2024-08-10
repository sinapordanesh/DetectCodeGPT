def find_most_frequent_and_longest(text):
    words = text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    most_frequent_word = max(word_count, key=word_count.get)
    longest_word = max(words, key=len)
    
    return most_frequent_word + " " + longest_word

# Test the function with the sample input
print(find_most_frequent_and_longest("Thank you for your mail and your lectures"))