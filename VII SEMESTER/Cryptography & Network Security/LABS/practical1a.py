class Cryptography:

    def __init__(self, key: int) -> None:
        self.__key: int = key
        self.__plain_text: str = ""
        self.__cypher_text: str = ""

    def encryption(self, input_string: str) -> None:
        for i in input_string:
            a: int = (ord(i) - 97 + self.__key)
            while a < 0:
                a += 26
            index: int = (a % 26)
            self.__cypher_text += chr(index + 65)
        self.display('Encryption', self.__cypher_text)

    def decryption(self, input_string: str) -> None:
        for i in input_string:
            a: int = (ord(i) - 65 - self.__key)
            while a < 0:
                a += 26
            index: int = (a % 26)
            self.__plain_text += chr(index + 97)
        self.display('Decryption', self.__plain_text)

    @staticmethod
    def display(method: str, text: str) -> None:
        print(f'\n{method} : {text}')
        
class VigenereCipher:
    def __init__(self) -> None:
        self.__plaintext: str = ""
        self.__cyphertext: str = ""
        self.__keyword: str = ""
        
    def encryption(self, plaintext: str, keyword: str) -> str:
        self.__plaintext = plaintext
        self.__keyword = "".join(keyword[i%len(keyword)] for i in range(len(self.__plaintext)))
        
        for i, v in enumerate(self.__plaintext):
            self.__cyphertext += chr(((ord(v) + ord(self.__keyword[i]) - 2*97) % 26) + 65)
        
        return self.__cyphertext
            
    def decryption(self,cyphertext: str, keyword: str) -> str:
        self.__cyphertext = cyphertext
        self.__keyword = "".join(keyword[i%len(keyword)] for i in range(len(self.__cyphertext)))
        self.__plaintext = ""
        
        for i, v in enumerate(self.__cyphertext):
            a: int = (ord(v) - 65) - (ord(self.__keyword[i]) - 97)
            while a < 0:
                a += 26
                  
            self.__plaintext += chr((a % 26) + 97)
        
        return self.__plaintext
        

def ask_choice(obj: Cryptography, input_string: str) -> None:
    choice: int = int(input('''
    1. Encrypt
    2. Decrypt
    Enter choice:'''))
    match choice:
        case 1:
            obj.encryption(input_string)
        case 2:
            obj.decryption(input_string)

def main() -> None:
    while True:
        choice: int = int(input('''
    1. Ceaser Cipher
    2. Modified Ceaser Cipher
    3. Vigenere Cipher
    0. Exit
    Enter Choice :'''))
        if not choice:
            break
        elif not 1 <= choice <= 3:
            print('\nInvalid Choice')
            continue
        input_string: str = input("Enter Your String :")
        match choice:
            case 1:
                ceaser_cipher: Cryptography = Cryptography(3)
                ask_choice(ceaser_cipher,input_string)
            case 2:
                key: int = int(input("Enter Your Key :"))
                modified_ceaser_cipher: Cryptography = Cryptography(key)
                ask_choice(modified_ceaser_cipher, input_string)
            case 3:
                keyword: str = input("Enter Your Keyword : ")
                vigenereCipher: VigenereCipher = VigenereCipher()
                encrpyted: str = vigenereCipher.encryption(input_string, keyword)
                decrypted: str = vigenereCipher.decryption(encrpyted, keyword)
                print('Encypted string :', encrpyted)
                print('Decrypted String :', decrypted)

if __name__ == '__main__':
    main()