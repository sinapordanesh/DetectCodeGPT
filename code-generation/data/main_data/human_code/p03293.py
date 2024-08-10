# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    S = input()
    T = input()

    return S, T


def main(S: str, T: str) -> None:
    """
    メイン処理.

    Args:\n
        S (str): 英子文字からなる文字列(2 <= |S| <= 100)
        T (str): 英子文字からなる文字列(|S| = |T|)
    """
    # 求解処理
    N = len(S)
    ans = "No"
    for i in range(N):
        if S[-i:] + S[:-i] == T:
            ans = "Yes"
            break

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    S, T = get_input()

    # メイン処理
    main(S, T)
