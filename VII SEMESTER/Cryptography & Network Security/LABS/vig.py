cipherMap : dict = {
    0: ['a','A'],
    1: ['b','B'],
    2: ['c','C'],
    3: ['d','D'],
    4: ['e','E'],
    5: ['f','F'],
    6: ['g','G'],
    7: ['h','H'],
    8: ['i','I'],
    9: ['j','J'],
    10: ['k','K'],
    11: ['l','L'],
    12: ['m','M'],
    13: ['n','N'],
    14: ['o','O'],
    15: ['p','P'],
    16: ['q','Q'],
    17: ['r','R'],
    18: ['s','S'],
    19: ['t','T'],
    20: ['u','U'],
    21: ['v','V'],
    22: ['w','W'],
    23: ['x','X'],
    24: ['y','Y'],
    25: ['z','Z'],
}


def ceaserEncryption(pt:str,key:int) -> str:
    ct = str()
    
    for i in pt:
        ct += cipherMap[(ord(i) - 97 + key) % 26][1]

    return ct


def ceaserDecryption(ct:str,key:int) -> str:
    pt = str()
    
    for i in ct:
        pt += cipherMap[(ord(i) - 65 - key) % 26][0]
        
    return pt


def ceaserCipher(t:bool) -> None:
    print('''
Press 1 for Encryption 
Press 2 for Decryption
          '''
          )
    toggle = int(input())
    if toggle == 1:
        print('Enter PlainText:')
        pt = str(input()).lower()
        if t:
            print('Shift Key:')
            k = int(input())
            print(ceaserEncryption(pt,k))
        else:
            print(ceaserEncryption(pt,k))
    elif toggle == 2:
        print('Enter CipherText:')
        ct = str(input()).upper()
        if t:
            print('Shift Key:')
            k = int(input())
            print(ceaserDecryption(ct,k))
        else:
            for i in range(0,25):
                print(ceaserDecryption(ct,i))
    else:
        exit()

       

def vigenereEncryption(pt:str, k:str):
    ct = str()
    size = len(k)
    j = 0
    for i in pt:
        if j > size - 1:
            j = j - size
            
        key = k[j]
        ct += chr((((ord(i) - 97) + (ord(key) - 65)) % 26) + 65)
        j += 1
    return ct

    
def vigenereDecryption(ct:str, k:str):
    pt = str()
    size = len(k)
    j = 0
    for i in ct:
        if j > size - 1:
            j = j - size
            
        key = k[j]
        pt += chr((((ord(i) - 65) - (ord(key) - 65)) % 26) + 97)
        j += 1
    return pt


def vigenereCipher():
    print('''
Press 1 for Encryption
Press 2 for Decryption
          ''')
    
    toggle = int(input())
    
    if toggle == 1:
        print('Enter PlainText:')
        pt = str(input()).lower()
        print('Enter Keyword:')
        k = str(input()).upper()
        print(f'''
CipherText: {vigenereEncryption(pt,k)}
            ''')
    elif toggle == 2:
        print('Enter CipherText:')
        ct = str(input()).upper()
        print('Enter Keyword:')
        k = str(input()).upper()
        print(f'''
PlainText: {vigenereDecryption(ct,k)}
            ''')
    else:
        exit()



def main() -> None:
    print('''
Press 1 to use Ceaser Cipher
Press 2 to use Modified Ceaser Cipher
Press 3 to use Vigenere Cipher
          ''')
    
    cToggle = int(input())
    
    if cToggle == 1:
        ceaserCipher(False)    
    elif cToggle == 2:
        ceaserCipher(True)
    elif cToggle == 3:
        vigenereCipher()
    else:
        exit()



if __name__ == "_main_":
    main()