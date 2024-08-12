import random

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

def hillCipher(text: str, matrix: list[int]):
    size: int = 2
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    flag: bool = False if text.islower() else True
    
    for i, v in enumerate(matrix):
        while v < 0:
            v += 26
        matrix[i] = v
    
    if flag: 
        text = text.lower()
        a, b, c, d = matrix
        det = ((a*d) - (b*c))
        while( det < 0):
            det += 26
        detinv = EEA(26, det)
        while(detinv < 0):
            detinv += 26
        adjoint = [d, -b, -c, a]
        for i, v in enumerate(adjoint):
            while v < 0:
                v += 26
            adjoint[i] = v
        for i, v in enumerate(adjoint):
            matrix[i] = v * detinv
         
    
    while(len(text) % size):
        text += random.choice("".join(ch for ch in alphabet if ch not in [*text]))
             
    textlist: list[str] = [text[i:i+size] for i in range(0,len(text),size)]
    
    result: str = ""
    for txt in textlist:
        plist: list[int] = list()
        for ch in txt:
            plist.append(alphabet.find(ch))
        x, y = plist
        a, b, c, d = matrix
        clist: list[int] = [(a*x + c*y)%26, (b*x + d*y)%26]
        for v in clist:
            result += alphabet[v]
        
    if flag:
        print("Decrypted:", result.lower())
    else:
        print("Encrypted:", result.upper())


def main() -> None:
    print(f'{'start':-^40}')
    matrix: list[int] = list(map(int, input("Enter Your Matrix a, b, c, d: ").strip().split(" ")))
    inputText: str = input("Enter Your String: ")
    print('-'*40)
    hillCipher(inputText, matrix)
    print(f'{'end':-^40}')

if __name__ == '__main__':
    main()