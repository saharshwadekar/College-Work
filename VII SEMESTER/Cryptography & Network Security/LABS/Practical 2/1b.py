import random
def simpleColumnar(inputText: str, column: int):
    row: int = (len(inputText) / column).__ceil__()

    if inputText.islower():
        while(len(inputText) < row*column):
            inputText += random.choice("".join(ch for ch in 'abcdefghijklmnopqrstuvwxyz' if ch not in [*inputText])) * (row*column - len(inputText)) 
        matrix: list[str] = [
            inputText[i : i + column] for i in range(0, len(inputText), column)
        ]
        
        encrypt: str = ""
        for text in matrix:
            print(*text, sep=" ")
            
        for i in range(column):
            for text in matrix:
                encrypt += text[i].upper()

        print('-'*40)
        print("Encrypted:", encrypt)
    else:
        while(len(inputText) < row*column):
            inputText += random.choice("".join(ch for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if ch not in [*inputText])) * (row*column - len(inputText)) 
        matrix: list[list[chr]] = [ list(" ") * column for r in range(row)]
        
        i: int = 0
        for c in range(column):
            for r in range(row):
                matrix[r][c] = inputText[i]
                i+=1
        
        for text in matrix:
            print(*text, sep=" ")
            
        decrypt: str = ""      
        for text in matrix:
            decrypt += ''.join(text).lower()
            
        print('-'*40)
        print("Decrypted:", decrypt)


def main() -> None:
    while True:
        print(f'{'start':-^40}')
        inputText: str = input("Enter your String :").replace(" ", "")
        column: int = int(input("Enter Column: "))
        print("-" * 40)
        simpleColumnar(inputText=inputText, column=column)
        print(f'{'end':-^40}')

if __name__ == "__main__":
    main()
