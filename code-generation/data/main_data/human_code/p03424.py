def decision(pack: list) -> str:
    if "Y" in pack:
        return "Four"
    return "Three"


if __name__ == "__main__":
    n = int(input())
    pack = list(map(str, input().split()))
    print(decision(pack))