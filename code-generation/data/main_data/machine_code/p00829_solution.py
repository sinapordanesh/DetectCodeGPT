def find_key(dataset):
    inputs = [int(x, 16) for x in dataset.split()]
    checksum = sum(inputs[:8]) % (2**32)
    last_input = inputs[8]
    
    if (checksum ^ last_input) & 1:
        return '1'
    else:
        return '0'