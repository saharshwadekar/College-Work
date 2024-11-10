import copy
def swap(sArray, i , j) -> None:
    sArray[i], sArray[j] = sArray[j], sArray[i]

def keyScheduling(sArray: list, tArray: list) -> list:
    j: int = 0
    size: int = len(sArray)
    for i in range(size):
        j = (j + sArray[i] + tArray[i])
        while j < 0:
            j += size
        j = j % size
        swap(sArray, i, j)
        
    return sArray

def Encryption(plainText: list, tArray: list) -> None:
    encrypt: list[int] = list()
    for p, k in zip(plainText, tArray):
        encrypt.append(p ^ k)
    return encrypt

def streamGeneration(sArray: list, plainText: list) -> list:
    print(f'{sArray=}')
    slen: int = len(sArray)
    size: int = len(plainText)
    i: int = 0
    j: int = 0
    key: list = list()
    for i in range(1, size + 1):
        j = (j + sArray[i]) % slen
        swap(sArray, i , j)
        t = (sArray[i] + sArray[j]) % slen
        print(f'{i=}, {j=}, {t=}, {sArray[t]=}, {sArray=}')
        key.append(sArray[t])
    return key
             
        

def main() -> None:
    try:
        sArray = list(map(int, input("Enter S-Array (in DEC format X X ...): ").split(" ")))
        plainText = list(map(int, input("Enter PlainText (in DEC format X X ...): ").split(" ")))
        key = list(map(int, input("Enter Key Array (in DEC format X X ...): ").split(" ")))
        tArray: list[int] = list()
        i: int = 0
        keysize: int = len(key)
        while(len(sArray) != len(tArray)):
            tArray.append(key[i])
            i = (i+1) % keysize
        
        sArray = keyScheduling(sArray, tArray)
        key = streamGeneration(sArray, plainText)
        encrypt = Encryption(plainText, key)
        
        print(f'Encrypted PlainText: {encrypt}')
        
    except Exception as e:
        print("Error in Handling ", e)
        
    
if __name__ == '__main__':
    main()