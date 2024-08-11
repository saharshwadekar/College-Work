def encrypt(inputText: str, key: int) -> str:
    i: int = 0;
    matrix: list[str] = ["" for _ in range(key)]
    flag: bool = True
    for ch in inputText:
        matrix[i] += ch
        if flag: i += 1
        else: i -= 1
        if i == key-1 or i == 0: flag = not(flag)
    print(matrix)
        
        
    return ''.join(matrix)
    
def decrypt(inputText: str, key:int) -> str:
    i: int = 0;
    div: int = len(inputText) // key
    matrix: list[str] = ["" for _ in range(key)]
    flag: bool = True
    for ch in inputText:
        matrix[i] += ch
        if flag: i += 1
        else: i -= 1
        if i == key-1 or i == 0: flag = not(flag)
    
    print(matrix)
        

def main() -> None:
    inputText: str = input("Enter your String :").strip().replace(" ", "")
    key: int = int(input("Enter Key: "))
    res = encrypt(inputText, key)
    print("Encrypt :", res)
    res = decrypt(res, key)
    print("Decrypt :", res)

if __name__ == '__main__':
    main()