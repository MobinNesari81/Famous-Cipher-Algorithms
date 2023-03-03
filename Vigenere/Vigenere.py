import numpy as np

# Define the Vigenere cipher class
class VigenereCipher:

    # Initialize the class with the given key
    def __init__(self, key):
        self.key = key

    # Generate the Vigenere table with the alphabet
    def generate_vigenere_table(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        table = np.zeros((26, 26), dtype=np.int32)
        for i in range(26):
            for j in range(26):
                table[i][j] = (i + j) % 26
        return table

    # Encrypt the given plaintext using Vigenere cipher
    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        key = self.key.upper()
        vigenere_table = self.generate_vigenere_table()
        ciphertext = ''
        key_index = 0
        for letter in plaintext:
            if letter.isalpha():
                row = ord(key[key_index]) - 65
                col = ord(letter) - 65
                ciphertext += chr(vigenere_table[row][col] + 65)
                key_index = (key_index + 1) % len(key)
            else:
                ciphertext += letter
        return ciphertext

    # Decrypt the given ciphertext using Vigenere cipher
    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        key = self.key.upper()
        vigenere_table = self.generate_vigenere_table()
        plaintext = ''
        key_index = 0
        for letter in ciphertext:
            if letter.isalpha():
                row = ord(key[key_index]) - 65
                col = (ord(letter) - 65 - row) % 26
                plaintext += chr(col + 65)
                key_index = (key_index + 1) % len(key)
            else:
                plaintext += letter
        return plaintext

