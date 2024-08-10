def keyboard_string(s):
    result = []
    for char in s:
        if char == '0':
            result.append('0')
        elif char == '1':
            result.append('1')
        elif char == 'B':
            if result:
                result.pop()
    return ''.join(result)