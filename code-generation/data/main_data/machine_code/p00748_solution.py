def tetrahedral_numbers():
    tetrahedral = [n * (n + 1) * (n + 2) // 6 for n in range(1, 181)]
    odd_tetrahedral = [n * (n + 1) * (n + 2) // 6 for n in range(1, 181) if n % 2 != 0]
    
    while True:
        num = int(input())
        if num == 0:
            break
        for i in range(len(tetrahedral)):
            if num <= tetrahedral[i]:
                print(i + 1, end=' ')
                break
        for i in range(len(odd_tetrahedral)):
            if num <= odd_tetrahedral[i]:
                print(i + 1)
                break

tetrahedral_numbers()