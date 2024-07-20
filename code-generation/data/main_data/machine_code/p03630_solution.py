def max_rectangle_area(H, W, S):
    result = 0
    row = [0] * W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                row[j] = 0
            else:
                row[j] += 1
        left = [0] * W
        right = [0] * W
        stack = []
        for j in range(W):
            while stack and row[stack[-1]] >= row[j]:
                stack.pop()
            if stack:
                left[j] = stack[-1] + 1
            else:
                left[j] = 0
            stack.append(j)
        stack = []
        for j in range(W - 1, -1, -1):
            while stack and row[stack[-1]] >= row[j]:
                stack.pop()
            if stack:
                right[j] = stack[-1] - 1
            else:
                right[j] = W - 1
            stack.append(j)
        for j in range(W):
            result = max(result, row[j] * (right[j] - left[j] + 1))
    return result

# Sample Input 1
print(max_rectangle_area(3, 3, ['..#', '##.', '.#.']))

# Sample Input 2
print(max_rectangle_area(4, 4, ['....', '....', '....', '....']))

# Sample Input 3
print(max_rectangle_area(10, 8, ['##...#.#', '##...#.#', '..###.#.', '#.##.#.#', '.#..#.#.', 
                                  '..##.#.#', '##.#.#..', '...#.#..', '###.#.##', '###..###']))