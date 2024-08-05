import random

class PlayfairCipher:
    def __init__(self, keyword: str):
        self.keyword = keyword.upper()
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        self.matrix = self._create_matrix()
    
    def _create_matrix(self):
        keyword = ''.join(sorted(set(self.keyword), key=self.keyword.index))  # Deduplicate keyword preserving order
        if 'I' in keyword:
            _ = 'J'
        else:
            _ = 'I'
        
        matrix_string = keyword + ''.join(ch for ch in self.alphabet if ch not in keyword and ch != _)
        return [list(matrix_string[i:i+5]) for i in range(0, 25, 5)]

    def _prepare_text(self, text: str) -> str:
        text = text.lower().replace('j', 'i')
        prepared_text = ''
        i = 0
        
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared_text += text[i] + random.choice(self.alphabet.replace(text[i].upper(), ''))
                i += 1
            else:
                prepared_text += text[i]
                i += 1
        
        if len(prepared_text) % 2 != 0:
            prepared_text += random.choice(self.alphabet.replace(prepared_text[-1].upper(), '')).lower()
        
        return prepared_text

    def _find_index(self, char1: str, char2: str):
        i1, j1 = [(i, row.index(char1)) for i, row in enumerate(self.matrix) if char1 in row][0]
        i2, j2 = [(i, row.index(char2)) for i, row in enumerate(self.matrix) if char2 in row][0]
        return i1, j1, i2, j2

    def _encrypt_pair(self, char1: str, char2: str) -> str:
        i1, j1, i2, j2 = self._find_index(char1.upper(), char2.upper())
        if i1 == i2:
            return self.matrix[i1][(j1 + 1) % 5] + self.matrix[i2][(j2 + 1) % 5]
        elif j1 == j2:
            return self.matrix[(i1 + 1) % 5][j1] + self.matrix[(i2 + 1) % 5][j2]
        else:
            return self.matrix[i1][j2] + self.matrix[i2][j1]

    def _decrypt_pair(self, char1: str, char2: str) -> str:
        i1, j1, i2, j2 = self._find_index(char1.upper(), char2.upper())
        if i1 == i2:
            return self.matrix[i1][(j1 - 1) % 5] + self.matrix[i2][(j2 - 1) % 5]
        elif j1 == j2:
            return self.matrix[(i1 - 1) % 5][j1] + self.matrix[(i2 - 1) % 5][j2]
        else:
            return self.matrix[i1][j2] + self.matrix[i2][j1]

    def encrypt(self, plaintext: str) -> str:
        prepared_text = self._prepare_text(plaintext)
        cipher_text = ''.join(self._encrypt_pair(prepared_text[i], prepared_text[i + 1]) for i in range(0, len(prepared_text), 2))
        return cipher_text.upper()

    def decrypt(self, ciphertext: str) -> str:
        prepared_text = self._prepare_text(ciphertext.lower())
        plain_text = ''.join(self._decrypt_pair(prepared_text[i], prepared_text[i + 1]) for i in range(0, len(prepared_text), 2))
        return plain_text.replace('j', 'i')

def main():
    keyword = input("Enter Your KEYWORD in capital: ")
    cipher = PlayfairCipher(keyword)
    
    while True:
        choice = input("Choose operation - Encrypt (E) / Decrypt (D): ").strip().upper()
        if choice not in ('E', 'D'):
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
            continue
        
        if choice == 'E':
            plaintext = input("Enter Your STRING in lowercase: ")
            result = cipher.encrypt(plaintext)
            print("Encrypted:", result)
        elif choice == 'D':
            ciphertext = input("Enter Your CIPHERTEXT in uppercase: ")
            result = cipher.decrypt(ciphertext)
            print("Decrypted:", result)

if __name__ == '__main__':
    main()
