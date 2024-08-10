def book_index():
    index = {}
    
    while True:
        try:
            word, page_number = input().split()
            page_number = int(page_number)
            
            if word in index:
                index[word].append(page_number)
            else:
                index[word] = [page_number]
        except:
            break
    
    for word in sorted(index.keys()):
        print(word)
        for page_number in sorted(index[word]):
            print(page_number, end=" ")
        print()

book_index()