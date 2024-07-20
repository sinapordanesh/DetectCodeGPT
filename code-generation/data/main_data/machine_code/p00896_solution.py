def decode_message():
    while True:
        n = int(input())
        if n == 0:
            break
        words = [input() for _ in range(n)]
        sequence = input().split()[:-1]
        decoded_message = []
        for word in sequence:
            for i in range(len(word)):
                for j in range(len(words)):
                    if word[:i+1] == words[j][:i+1]:
                        decoded_message.append(words[j])
                        break
        if len(decoded_message) == len(sequence):
            print(' '.join(decoded_message) + '.')
        else:
            print('-.')

decode_message()