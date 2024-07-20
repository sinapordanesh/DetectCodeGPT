def main():
    S = input()
    size = [[[[0, 0]], []], [[], []]]
    length = 0

    for s in S:
        size2 = [[[], []], [[], []], [[], []]]
        if s != "0":
            for i in range(2):
                for j in range(2):
                    if size[i][j]:
                        for x, y in size[i][j]:
                            if y == length+i:
                                size2[i+1][j ^ 1].append([y+1, y+1])
                                if x != y:
                                    size2[i][j ^ 1].append([x+1, y-1])
                            else:
                                size2[i][j ^ 1].append([x+1, y+1])
        if s != "1":
            for i in range(2):
                for j in range(2):
                    if size[i][j]:
                        for x, y in size[i][j]:
                            if x == 0:
                                size2[i+1][j].append([0, 0])
                                if x != y:
                                    size2[i][j ^ 1].append([x+1, y-1])
                            else:
                                size2[i][j ^ 1].append([x-1, y-1])
        if len(size2[0][0]+size2[0][1]) == 0:
            size2 = size2[1:]
            length += 1
        else:
            size2.pop()
        for i in range(2):
            for j in range(2):
                size2[i][j] = sorted(size2[i][j])
        size = [[[], []], [[], []]]
        for i in range(2):
            for j in range(2):
                if len(size2[i][j]) == 0:
                    continue
                size[i][j] = [size2[i][j][0]]
                for x, y in size2[i][j][1:]:
                    size[i][j][-1][1] = max(y, size[i][j][-1][1])

    print(length)


main()
