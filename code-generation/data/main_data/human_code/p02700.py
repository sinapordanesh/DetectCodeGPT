'''
問題：
    高橋君と青木君がモンスターを闘わせます。

    高橋君のモンスターは体力が A で攻撃力が B です。
    青木君のモンスターは体力が C で攻撃力が D です。

    高橋君→青木君→高橋君→青木君→... の順に攻撃を行います。
    攻撃とは、相手のモンスターの体力の値を自分のモンスターの攻撃力のぶんだけ減らすことをいいます。
    このことをどちらかのモンスターの体力が 0 以下になるまで続けたとき、
    先に自分のモンスターの体力が 0 以下になった方の負け、そうでない方の勝ちです。

    高橋君が勝つなら Yes、負けるなら No を出力してください。
'''

'''
制約：
    1 ≦ A, B, C, D ≦ 100
    入力は全て整数である
'''
class Monster:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, power)  -> int:
        self.hp -= power
        return self.hp

    def is_loser(self)   -> bool:
        return self.hp <= 0

# 標準入力から A, B, C, D を取得する
a, b, c, d = map(int, input().split())

takahashi_monster = Monster(a, b)   # 高橋モンスター
aoki_monster = Monster(c, d)    # 青木モンスター
result = "ret"

while True:
    aoki_monster.fight(b)   # 高橋の攻撃
    if aoki_monster.is_loser():
        result = "Yes"
        break

    takahashi_monster.fight(d)  # 青木の攻撃
    if takahashi_monster.is_loser():
        result = "No"
        break

print(result)
