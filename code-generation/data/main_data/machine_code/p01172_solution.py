def recurring_fraction():
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        decimal_part = []
        remainders = {}
        recurring_start = -1
        recurring_length = 0
        remainder = x % y
        
        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = len(decimal_part)
            x = remainder * 10
            decimal_part.append(str(x // y))
            remainder = x % y
        
        if remainder != 0:
            recurring_start = remainders[remainder]
            recurring_length = len(decimal_part) - recurring_start
        
        print(recurring_start, recurring_length)

recurring_fraction()