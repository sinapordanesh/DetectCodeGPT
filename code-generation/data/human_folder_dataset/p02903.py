def main():
    H, W, A, B = map(int, input().split())
    for _ in range(B):
        tmp = ['0']*A + ['1']*(W-A)
        print(''.join(tmp))
    
    for _ in range(H-B):
        tmp = ['1']*A + ['0']*(W-A)
        print(''.join(tmp))
    
if __name__ == "__main__":
    main()
