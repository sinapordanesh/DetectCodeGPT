def distorted_love(n, pages):
    for page in pages:
        current_page = page[0]
        buffer = [current_page]
        pointer = 0
        
        for operation in page[1]:
            if operation[0] == 'click':
                x, y = operation[1], operation[2]
                for button in page[1]:
                    if button[0] <= x <= button[2] and button[1] <= y <= button[3]:
                        buffer = buffer[:pointer+1]
                        buffer.append(button[4])
                        pointer += 1
                        break
            elif operation[0] == 'back':
                if pointer > 0:
                    pointer -= 1
            elif operation[0] == 'forward':
                if pointer < len(buffer) - 1:
                    pointer += 1
            elif operation[0] == 'show':
                print(buffer[pointer])
                
        print('')

n = 3
pages = [
    ("index", [(1, 500, 100, 700, 200),]),
    ("profile", [(2, 100, 100, 400, 200, "index"), (100, 400, 400, 500, "link"),]),
    ("link", [(1, 100, 100, 300, 200, "index"),])
]

distorted_love(n, pages)