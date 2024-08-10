def hat_color(N, s):
    count_red = s.count('R')
    count_blue = s.count('B')
    
    if count_red > count_blue:
        return 'Yes'
    else:
        return 'No'