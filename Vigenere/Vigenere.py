import numpy as np


# Define the Vigenere cipher class
class VigenereCipher:

    # Initialize the class with the given key
    def __init__(self, key: str) -> None:
        self.key = key

    # Generate the Vigenere table with the alphabet
    def __generate_vigenere_table(self) -> np.ndarray[np.uint8]:
        table = np.zeros((26, 26), dtype=np.uint8)
        for i in range(26):
            for j in range(26):
                table[i][j] = (i + j) % 26
        return table

    # Encrypt the given plaintext using Vigenere cipher
    def encrypt(self, plaintext: str) -> str:
        key = self.key.upper()
        key_length = len(key)
        vigenere_table = self.__generate_vigenere_table()
        ciphertext = ''
        key_index = 0
        for letter in plaintext.upper():
            if letter.isalpha():
                row = ord(key[key_index]) - 65
                col = ord(letter) - 65
                ciphertext += chr(vigenere_table[row][col] + 65)
                key_index += 1
                if key_index == key_length:
                    key_index = 0
            else:
                ciphertext += letter
        return ciphertext

    # Decrypt the given ciphertext using Vigenere cipher
    def decrypt(self, ciphertext: str) -> str:
        ciphertext = ciphertext.upper()
        key = self.key.upper()
        key_length = len(key)
        plaintext = ''
        key_index = 0
        for letter in ciphertext:
            if letter.isalpha():
                row = ord(key[key_index]) - 65
                col = (ord(letter) - 65 - row) % 26
                plaintext += chr(col + 65)
                key_index += 1
                if key_index == key_length:
                    key_index = 0
            else:
                plaintext += letter
        return plaintext
