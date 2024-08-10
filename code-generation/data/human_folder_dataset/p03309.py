# -*- coding: utf-8 -*-
# モジュールのインポート
import statistics


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    A = list(map(int, input().split()))

    return N, A


def main(N: int, A: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 整数列の長さ(1 <= N <= 2 × 10^5)
        A (list): 整数列(1 <= A_i <= 10^9)
    """
    # 求解処理
    B = [A[i] - (i + 1) for i in range(N)]
    b = statistics.median_high(B)
    ans = sum([abs(B[i] - b) for i in range(N)])

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, A = get_input()

    # メイン処理
    main(N, A)
