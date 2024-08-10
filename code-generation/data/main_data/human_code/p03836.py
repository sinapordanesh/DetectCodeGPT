def main():
    sx, sy, tx, ty = map(int, input().split())
    x = tx - sx
    y = ty - sy
    s = "R"*x + "U"*y
    s += s.translate(str.maketrans({"U": "D",
                                    "D": "U", "L": "R", "R": "L"}))
    tmp = "D" + "R"*(x+1) + "U"*(y+1) + "L"
    s += tmp + tmp.translate(str.maketrans({"U": "D",
                                            "D": "U", "L": "R", "R": "L"}))
    print(s)


if __name__ == "__main__":
    main()
