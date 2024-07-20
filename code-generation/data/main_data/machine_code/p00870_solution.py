def search_concatenated_strings():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        element_strings = [input() for _ in range(n)]
        text = ''.join([input() for _ in range(m)])
        count = 0
        for i in range(len(text)):
            for j in range(n):
                if text[i:i + len(element_strings[j])] == element_strings[j]:
                    count += 1
                    break
        print(count)

search_concatenated_strings()