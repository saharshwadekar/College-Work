def simpleColumnar(inputText: str, column: int):
    row: int = (len(inputText) / column).__ceil__()
    while len(inputText) < row * column:
        inputText += "&"
    if inputText.islower():
        matrix: list[str] = [
            inputText[i : i + column] for i in range(0, len(inputText), column)
        ]
        encrypt: str = ""
        for text in matrix:
            print(*text, sep=" ")
        for i in range(column):
            for text in matrix:
                encrypt += text[i].upper()

        print(encrypt)
    else:
        matrix: list[str] = [
            inputText[i : i + row] for i in range(0, len(inputText), row)
        ]
        print(matrix)
        decrypt: str = ""
        for text in matrix:
            print(*text, sep=" ")
        for i in range(row):
            for text in matrix:
                decrypt += text[i].lower()
        print(decrypt)


def main() -> None:
    while True:
        inputText: str = input("Enter your String :").replace(" ","")
        print(inputText)
        column: int = int(input("Enter Column: "))
        simpleColumnar(inputText=inputText, column=column)


if __name__ == "__main__":
    main()
