def encrypt(inputText: str, key: int) -> str:
    matrix: list[list[chr]] = [list(" ") * len(inputText) for _ in range(key)]
    i: int = 0
    flag: bool = True
    for j, ch in enumerate(inputText):
        matrix[i][j] = ch
        if flag:
            i += 1
        else:
            i -= 1
        if i == key - 1 or i == 0:
            flag = not (flag)

    for row in matrix:
        print(*row)

    result: str = ""
    for row in matrix:
        result += "".join(row).replace(" ", "").upper()

    return result


def decrypt(inputText: str, key: int) -> str:
    matrix: list[list[chr]] = [list(" ") * len(inputText) for _ in range(key)]
    result: list[str] = [" " for _ in range(len(inputText))]

    ch: int = 0
    for row in range(key):
        i: int = 0
        flag: bool = True
        for x in range(len(inputText)):
            if i == row:
                matrix[row][x] = inputText[ch]
                result[x] = inputText[ch].lower()
                ch += 1
            if flag:
                i += 1
            else:
                i -= 1
            if i == key - 1 or i == 0:
                flag = not (flag)

    for row in matrix:
        print(*row)

    return "".join(result).replace(" ", "")


def main() -> None:
    inputText: str = input("Enter your String :").strip().replace(" ", "")
    key: int = int(input("Enter Key: "))

    if inputText.islower():
        print("-" * 40)
        res = encrypt(inputText, key)
        print("-" * 40)
        print("Encrypt :", res)
        print("-" * 40)
    else:
        print("-" * 40)
        res = decrypt(inputText, key)
        print("-" * 40)
        print("Decrypt :", res)
        print("-" * 40)


if __name__ == "__main__":
    main()
