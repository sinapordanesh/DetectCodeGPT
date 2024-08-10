def colored_cubes(dataset):
    n = dataset[0]
    cubes = dataset[1:]
    repaint = []
    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for k in range(6):
                if cubes[i][k] != cubes[j][k]:
                    count += 1
            repaint.append(count)
    return min(repaint)

data = [(3, ['scarlet green blue yellow magenta cyan', 'blue pink green magenta cyan lemon', 'purple red blue yellow cyan green']),
        (2, ['red green blue yellow magenta cyan', 'cyan green blue yellow magenta red']),
        (2, ['red green gray gray magenta cyan', 'cyan green gray gray magenta red']),
        (2, ['red green blue yellow magenta cyan', 'magenta red blue yellow cyan green']),
        (3, ['red green blue yellow magenta cyan', 'cyan green blue yellow magenta red', 'magenta red blue yellow cyan green']),
        (3, ['blue green green green green blue', 'green blue blue green green green', 'green green green green green sea-green']),
        (3, ['red yellow red yellow red yellow', 'red red yellow yellow red yellow', 'red red red red red red']),
        (4, ['violet violet salmon salmon salmon salmon', 'violet salmon salmon salmon salmon violet', 'violet violet salmon salmon violet violet', 'violet violet violet violet salmon salmon']),
        (1, ['red green blue yellow magenta cyan']),
        (4, ['magenta pink red scarlet vermilion wine-red', 'aquamarine blue cyan indigo sky-blue turquoise-blue', 'blond cream chrome-yellow lemon olive yellow', 'chrome-green emerald-green green olive vilidian sky-blue'])]

for dataset in data:
    print(colored_cubes(dataset))