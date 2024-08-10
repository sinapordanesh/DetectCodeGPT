def main():
    k, a, b = input_list()

    # たたきルート１手１枚増える
    # 交換ルートは2手必要
    if b - a > 2:
        # bisketをA枚にする
        bis = a
        k -= a - 1
        
        if k % 2 == 1:
            bis += 1
            k -= 1
        bis += (k//2) * (b-a)
        print(bis)
    else:
        print(k+1)

def input_list():
    return map(int, input().split())

if __name__ == "__main__":
    main()