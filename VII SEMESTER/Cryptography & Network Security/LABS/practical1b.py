import random

def playfair(inputstring, keyword):
    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nkey = ""
    for i in keyword:
        if i not in nkey:
            nkey =+ i
            
    print(nkey)
    
    _: chr = 'I'if 'I' in keyword else 'J'
    other: str = keyword + ''.join(ch for ch in alphabet if ch not in keyword and ch != _)
    matrix: list[list[str]] = [[*other[i:i+5]] for i in range(0,25,5)]

    _: chr = 'J' if 'I' in inputstring else 'I'
    remain: str = ''.join(ch for ch in alphabet if ch not in inputstring and ch != _)
    bogus: chr = random.choice([*remain])
 
    calcstring: str = ''
    j: int = 0
    for v in inputstring:
        ch: chr = v
        if j%2 and j != 0 and v == calcstring[j-1]:
            ch = bogus + v
            j+=2
        else:
            j+=1
        calcstring += ch

    if len(calcstring) % 2:
        calcstring += bogus

    calcmat: list[list[str]] = [[*calcstring[i:i+2]] for i in range(0,len(calcstring),2)]
    encipher: list[list[str]] = []
    
    for element in calcmat:
        i, j, x, y = findIndex(element=element, matrix=matrix)
        if i == x:
            encipher.append([matrix[i][(j+1)%5] , matrix[x][(y+1)%5]])
        elif j == y:
            encipher.append([matrix[(i+1)%5][j] , matrix[(x+1)%5][y]])
        else:
            encipher.append([matrix[i][y] , matrix[j][x]])
            
    return encipher


def findIndex(element: list[str], matrix):
    a, b, c, d = 0,0,0,0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element[0]:
                a = i
                b = j
            if matrix[i][j] == element[1]:
                c = i
                d = j
        print(end='\n')
    return a, b, c, d
    

def main() -> None:
    plain_text: str = input("Enter Your STRING in capital : ")
    plain_text = plain_text.upper()
    keyword: str = input("Enter Your KEYWORD in capital : ")
    keyword = keyword.upper()
    result = playfair(plain_text,keyword)
    print(result)
 
    
if __name__ == '__main__':
    main()