
def main():
    N = int(input())
    R = [-1] * (N+1)
    A = list(map(int,input().split()))
    for idx, a in enumerate(A):
        R[a] = idx+1

    for idx in range(1, len(R)):
        print(R[idx], end=" ")
    print("\n")
    

if __name__ == "__main__":
    main()

