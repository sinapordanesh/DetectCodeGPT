def equals_are_equals():
    while True:
        block = []
        while True:
            expr = input()
            if expr == '.':
                break
            block.append(expr)
        
        if len(block) == 0:
            break
        
        correct_answer = block[0]
        for answer in block[1:]:
            if eval(correct_answer.replace('^', '**').replace(' ', '')) == eval(answer.replace('^', '**').replace(' ', '')):
                print('yes')
            else:
                print('no')
        print('.')

equals_are_equals()