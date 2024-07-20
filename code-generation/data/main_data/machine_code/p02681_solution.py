def register_id(S, T):
    if T == S + 'z':
        print('Yes')
    else:
        print('No') 

#Sample Input 1
register_id('chokudai', 'chokudaiz')

#Sample Input 2
register_id('snuke', 'snekee')

#Sample Input 3
register_id('a', 'aa')