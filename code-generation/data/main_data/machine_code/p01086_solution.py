def find_short_phrase():
    while True:
        n = int(input())
        if n == 0:
            break
        words = []
        for _ in range(n):
            words.append(input())
        
        total_letters = [len(word) for word in words]
        
        for i in range(n):
            if i + 1 < n - 4:
                if sum(total_letters[i:i+5]) == 5 and sum(total_letters[i+5:i+12]) == 7 and total_letters[i+12] == 5 and total_letters[i+13] == 7 and total_letters[i+14] == 7:
                    print(i+1)
                    break

find_short_phrase()