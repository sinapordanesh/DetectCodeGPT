
def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt_A = 0
    cnt_B = 0
    for i in range(N):
        if A[i] > B[i]:
            cnt_A += A[i] - B[i]
        if B[i] > A[i]:
            cnt_B += (B[i] - A[i]) // 2

    if cnt_B >= cnt_A:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    resolve()
