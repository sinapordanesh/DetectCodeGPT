#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    # 入力
    N = int(raw_input())

    inp = []
    for x in range(N):
        input_list = raw_input()
        inp.append(input_list)

    # 文字列置換
    for x in inp:
        replaced = x.replace("Hoshino", "Hoshina")
        print(replaced)

if __name__=='__main__':
    main()