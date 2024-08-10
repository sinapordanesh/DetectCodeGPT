def is_idempotent(filter):
    for i in range(128):
        if filter[i] != filter[int(bin(i)[2:].zfill(7)[3], 2)]:
            return "no"
    return "yes"