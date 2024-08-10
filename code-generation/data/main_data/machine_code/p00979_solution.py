def fast_forwarding(t):
    time = 0
    
    while t > 0:
        if t % 3 == 0:
            t //= 3
        else:
            t -= 1
        time += 1
    
    return time