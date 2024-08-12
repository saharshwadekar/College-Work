def EEA(a: int, b: int) -> int:
    r1: int = a
    r2: int = b
    t1: int = 0
    t2: int = 1
    while r2 > 0:
        q: int = r1 // r2
        r: int = r1 - q * r2
        r1, r2 = r2, r
        t: int = t1 - q * t2
        t1, t2 = t2, t
    return t1


def multiplicativeCipher(inputText: str, key: int):
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    result: str = ""
    if inputText.islower():
        for ch in inputText:
            result += alphabet[(alphabet.find(ch) * key) % 26].upper()
        print("Encrypted:", result)
    else:
        t = EEA(26, key)
        while t < 0:
            t += 26
        for ch in inputText.lower():
            result += alphabet[(alphabet.find(ch) * t) % 26].lower()
        print("Decrypted:", result)
        
def AffineCipher(inputText: str, k1: int, k2: int):
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    result: str = ""
    if inputText.islower():
        for ch in inputText: 
            result += alphabet[((alphabet.find(ch) * k1) + k2) % 26]
        print("Encrypted:", result.upper())
    else:
        inputText = inputText.lower()
        k1 = EEA(26, k1)
        k2 = 26 - k2
        while k2 < 0:
            k2 += 26
        while k1 < 0:
            k1 += 26
        print(f'{k1=}')
        print(f'{k2=}')
        for ch in inputText:
            result += alphabet[((alphabet.find(ch) + k2) * k1) % 26]
        print("Decrypted:", result.lower())


def main() -> None:
    print(f'{'start':-^40}')

    choice: str = input('''(M) for Multiplicative Cipher\n(A) for Affine Cipher\nEnter Your Choice: ''').lower()
    match choice:
        case 'm':
            print('-'*40)
            inputText: str = input("Enter Your Text: ")
            key: int = int(input("Enter Your Key: "))
            print('-'*40)
            multiplicativeCipher(inputText, key)
        case 'a':
            print('-'*40)
            inputText: str = input("Enter Your Text: ")
            k1: int = int(input("Enter Key1: "))
            k2: int = int(input("Enter Key2: "))
            print('-'*40)
            AffineCipher(inputText, k1, k2)
    
    print(f'{'end':-^40}')
    

if __name__ == "__main__":
    main()
