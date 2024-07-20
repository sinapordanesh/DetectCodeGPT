def daruma_otoshi():
    while True:
        n = int(input())
        if n == 0:
            break
        blocks = list(map(int, input().split()))
        count = 0
        for i in range(1, n-1):
            if blocks[i] == blocks[i-1] or blocks[i] == blocks[i+1]:
                count += 1
                blocks.pop(i)
                blocks.pop(i)
                n -= 2
        print(count)

daruma_otoshi()