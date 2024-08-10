def check_futon_arrangement(datasets):
    for dataset in datasets:
        if dataset == 0:
            break
        futons = []
        for _ in range(dataset):
            x, y, direction = input().split()
            x, y = int(x), int(y)
            if direction == 'x':
                futons.append((x, y, x + 1, y))
            else:
                futons.append((x, y, x, y + 1))

        for i in range(len(futons)):
            for j in range(i + 1, len(futons)):
                if abs(futons[i][0] - futons[j][0]) <= 1 and abs(futons[i][1] - futons[j][1]) <= 1:
                    print("No")
                    break
            else:
                continue
            break
        else:
            print("Yes")