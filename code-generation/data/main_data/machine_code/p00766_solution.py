def chocolate_pieces(h, w, chocolate):
    pieces = 0
    for i in range(h):
        for j in range(w):
            if chocolate[i][j] == '#':
                pieces += 1
                if i < h-1 and chocolate[i+1][j] == '#':
                    pieces -= 1
                if j < w-1 and chocolate[i][j+1] == '#':
                    pieces -= 1
    return pieces

# Sample Input
print(chocolate_pieces(3, 5, ["###.#", "#####", "###.."]))
print(chocolate_pieces(4, 5, [".#.##", ".####", "####.", "##.#."]))
print(chocolate_pieces(8, 8, [".#.#.#.#", "########", ".######.", "########", ".######.", "########", ".######.", "########"]))
print(chocolate_pieces(8, 8, [".#.#.#.#", "########", ".##.#.#.", "##....##", ".##.###.", "##...###", ".##.###.", "###.#.##"]))
print(chocolate_pieces(4, 4, ["####", "####", "####", "####"]))