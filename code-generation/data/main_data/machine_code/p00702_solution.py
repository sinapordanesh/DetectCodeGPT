def analyze_kanglish(n, sentences):
    pairs = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            for i in range(len(word)-1):
                pair = word[i:i+2]
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
    
    kan_order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'ld', 'mb', 'mp', 'nc', 'nd', 'ng', 'nt', 'nw', 'ps', 'qu', 'cw', 'ts']
    
    result = []
    for i, char in enumerate(kan_order):
        if char in pairs:
            most_common = max(pairs, key=pairs.get)
            result.append(f"{char} {most_common} {pairs[most_common]}")
        else:
            result.append(f"{char} a 0")
    
    return result

# Sample Input
n = 3
sentences = ["nai tiruvantel ar varyuvantel i valar tielyama nu vilya", 
             "qua ist qda quang ncw psts", 
             "svampti tsuldya jay quadal ciszeriol"]

output = analyze_kanglish(n, sentences)
for line in output:
    print(line)