def main():
    a, b, c, k = map(int, input().split())

    if k % 2 == 1:
        print(b - a)
    else:
        print(a - b)


'''
    for i in range(k):
        temp_a = a
        temp_b = b
        temp_c = c

        a = temp_b + temp_c
        b = temp_a + temp_c
        c = temp_a + temp_b

    answer = a - b
    if answer > 10**18:
        print('Unfair')
    else:
        print(answer)
'''

if __name__ == '__main__':
    main()