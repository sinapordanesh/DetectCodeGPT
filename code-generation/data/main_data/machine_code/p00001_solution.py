def top_three_hills():
    mountains = []
    for _ in range(10):
        mountains.append(int(input()))

    mountains.sort(reverse=True)

    print(mountains[0])
    print(mountains[1])
    print(mountains[2])