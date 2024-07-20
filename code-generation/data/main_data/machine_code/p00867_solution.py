def digits_on_floor():
    result = []
    
    while True:
        n = int(input())
        if n == 0:
            break
        
        digits = [0]*10
        
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == x2:
                if y1 < y2:
                    digits[2] += 1
                else:
                    digits[5] += 1
            elif y1 == y2:
                if x1 < x2:
                    digits[1] += 1
                else:
                    digits[7] += 1
            elif x1 < x2 and y1 < y2:
                digits[3] += 1
            elif x1 > x2 and y1 < y2:
                digits[4] += 1
            elif x1 > x2 and y1 > y2:
                digits[6] += 1
            elif x1 < x2 and y1 > y2:
                digits[9] += 1
            else:
                digits[8] += 1
        
        result.append(digits)
    
    for digits in result:
        print(" ".join(map(str, digits)))