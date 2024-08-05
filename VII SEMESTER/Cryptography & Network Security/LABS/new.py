class vigenereCipher:
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
        
        
def main() -> None:
    onk = vigenereCipher()
    encrypt = onk.encryption("sheislistening","pascal")
    print(encrypt)
    decrypt = onk.decryption(encrypt,"pascal")
    print(decrypt)

if __name__ == '__main__':
    main()