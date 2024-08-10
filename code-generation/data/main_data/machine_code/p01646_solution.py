def lex_order():
    while True:
        n = int(input())
        if n == 0:
            break
        
        words = [input() for _ in range(n)]
        
        sorted_words = sorted(words)
        
        if words == sorted_words:
            print("yes")
        else:
            print("no")

lex_order()