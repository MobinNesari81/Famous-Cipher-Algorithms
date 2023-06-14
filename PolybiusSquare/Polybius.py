from typing import Tuple


class PolybiusSquareCipher:
    def __init__(self) -> None:
        """
        Initializes an instance of the PolybiusSquareCipher class with a 5x5 square
        containing the letters A to Z except J where I is used instead.
        """
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.square = [["A", "B", "C", "D", "E"],
                       ["F", "G", "H", "I", "K"],
                       ["L", "M", "N", "O", "P"],
                       ["Q", "R", "S", "T", "U"],
                       ["V", "W", "X", "Y", "Z"]]
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using the Polybius square cipher.

        Parameters:
        plaintext (str): The text to be encrypted.

        Returns:
        str: The encrypted ciphertext.
        """
        ciphertext = ""
        for char in plaintext.upper():
            if char == "J":
                char = "I"
            if char in self.alphabet:
                row, col = self.find_char(char)
                ciphertext += str(row) + str(col)
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the Polybius square cipher.

        Parameters:
        ciphertext (str): The text to be decrypted.

        Returns:
        str: The decrypted plaintext.
        """
        plaintext = ""
        i = 0
        while i < len(ciphertext):
            row = int(ciphertext[i])
            col = int(ciphertext[i+1])
            plaintext += self.square[row-1][col-1]
            i += 2
        return plaintext
    
    def find_char(self, char: str) -> Tuple[int, int]:
        """
        Finds the row and column of a given character in the Polybius square.

        Parameters:
        char (str): The character to be found in the square.

        Returns:
        tuple: A tuple containing the row and column indices of the character.
        """
        for i in range(len(self.square)):
            for j in range(len(self.square[i])):
                if self.square[i][j] == char:
                    return i+1, j+1
