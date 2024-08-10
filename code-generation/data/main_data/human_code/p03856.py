def main():
    import sys
    input = sys.stdin.readline
    
    S = input().rstrip()

    limit = len(S)//5

    while limit>0 and len(S)>0:
        if S.endswith('dreamer'):
            S = S[:len(S)-7]
        elif S.endswith('eraser'):
            S = S[:len(S)-6]
        elif S.endswith('dream'):
            S = S[:len(S)-5]
        elif S.endswith('erase'):
            S = S[:len(S)-5]
        limit-=1
    
    print('NO' if S else 'YES')

if __name__=='__main__':
    main()