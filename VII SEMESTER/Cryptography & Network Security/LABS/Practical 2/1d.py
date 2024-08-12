def hybridTransposition(inputText: str, enkey: list[list[int]]) -> None:
    enkey: list[list[int]] = list(map(list, enumerate(enkey, start=1)))
    dekey: list[list[int]] = sorted(enkey, key=lambda x: x[1])

    col: int = len(enkey)
    row: int = (len(inputText) / col).__ceil__()
    inputText += "*" * ((row * col) - len(inputText))

    enkey: list[int] = [x[1] for x in enkey]
    dekey: list[int] = [x[0] for x in dekey]

    result = ""

    if inputText.islower():
        print(f'Encrypted Key: ', enkey)
        print('-'*40)
        
        matrix: list[list[chr]] = [
            inputText[x : x + col] for x in range(0, len(inputText), col)
        ]
        for text in matrix:
            print(*text, sep=" ")
        print('-'*40)

        for e in enkey:
            for l in matrix:
                result += l[e - 1].upper()
        
        print(f'Encrypted: ',result)
    else:
        print(f'Decrypted Key: ', dekey)
        print('-'*40)
        
        matrix: list[list[chr]] = [ list(" ") * col for r in range(row)]
        
        i: int = 0
        for c in range(col):
            for r in range(row):
                matrix[r][c] = inputText[i]
                i+=1

        for text in matrix:
            print(*text, sep=" ")
        print('-'*40)
            
        for l in matrix:
            for d in dekey:
                result += l[d - 1].lower()
                
        print(f'Decrypted: ',result)


def main() -> None:
    print(f'{'start':-^40}')
    inputText: str = input("Enter your String :").strip().replace(" ", "")
    enkey: list[int] = map(int, input("Enter Your key: ").strip().split(" "))
    print('-'*40)
    hybridTransposition(inputText, enkey)
    print(f'{'end':-^40}')


if __name__ == "__main__":
    main()
