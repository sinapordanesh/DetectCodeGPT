def count_valid_plates(N, H, W, plates):
    count = 0
    for A, B in plates:
        if (A >= H and B >= W) or (A >= W and B >= H):
            count += 1
    return count

# Sample Input 1
N = 3
H = 5
W = 2
plates = [(10, 3), (5, 2), (2, 5)]
print(count_valid_plates(N, H, W, plates))

# Sample Input 2
N = 10
H = 587586158
W = 185430194
plates = [(894597290, 708587790), (680395892, 306946994), (590262034, 785368612), (922328576, 106880540), (847058850, 326169610), (936315062, 193149191), (702035777, 223363392), (11672949, 146832978), (779291680, 334178158), (615808191, 701464268)]
print(count_valid_plates(N, H, W, plates))