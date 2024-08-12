def func(inputText: str, enkey: list[list[int]]) -> str:
    enkey: list[list[int]] = list(map(list, enumerate(enkey, start=1)))
    dekey: list[list[int]] = sorted(enkey, key=lambda x: x[1])

    col: int = len(enkey)
    row: int = (len(inputText) / col).__ceil__()
    inputText += "*" * ((row * col) - len(inputText))

    enkey: list[int] = [x[1] for x in enkey]
    dekey: list[int] = [x[0] for x in dekey]
    print(f'Encrypted Key: ', enkey)
    print(f'Decrypted Key: ', dekey)

    result = ""

    if inputText.islower():
        matrix: list[list[chr]] = [
            inputText[x : x + col] for x in range(0, len(inputText), col)
        ]
        for text in matrix:
            print(*text, sep=" ")

        for e in enkey:
            for l in matrix:
                result += l[e - 1].upper()
                
        return result
    else:
        matrix: list[list[chr]] = [ list(" ") * col for r in range(row)]
        
        i: int = 0
        for c in range(col):
            for r in range(row):
                matrix[r][c] = inputText[i]
                i+=1
                
        for text in matrix:
            print(*text, sep=" ")
            
        for l in matrix:
            for d in dekey:
                result += l[d - 1].lower()
                
        return result


def main() -> None:
    inputText: str = input("Enter your String :").strip().replace(" ", "")

    enkey: list[int] = map(int, input("Enter Your key: ").strip().split(" "))
    result = func(inputText, enkey)
    print(f"{result=}")


if __name__ == "__main__":
    main()
