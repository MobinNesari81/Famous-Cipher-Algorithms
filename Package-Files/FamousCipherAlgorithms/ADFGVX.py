import random

class ADFGVXCipher:
    def __init__(self, key):
        """
        Initializes an instance of the ADFGVX Cipher class.

        Args:
            key (str): The encryption key used for generating the substitution table.

        Returns:
            None.
        """
        self.key = key.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.adfgvx = "ADFGVX"
        self.substitution_table = self.generate_substitution_table()

    def generate_substitution_table(self):
        """
        Generates a 6x6 substitution table based on the encryption key.

        Returns:
            List[List[str]]: A 6x6 substitution table where each element is a character from the alphabet.
        """
        key_chars = list(set(self.key))
        key_chars_sorted = sorted(key_chars)
        table = [[None for _ in range(6)] for _ in range(6)]
        for i, char in enumerate(key_chars_sorted):
            row = i // 6
            col = i % 6
            table[row][col] = char
        remaining_chars = [c for c in self.alphabet if c not in key_chars]
        random.shuffle(remaining_chars)
        for i, char in enumerate(remaining_chars):
            row = (i + len(key_chars)) // 6
            col = (i + len(key_chars)) % 6
            table[row][col] = char
        return table

    def encrypt(self, plaintext):
        """
        Encrypts the given plaintext using the ADFGVX Cipher algorithm.

        Args:
            plaintext (str): The plaintext to be encrypted.

        Returns:
            str: The ciphertext generated from the plaintext.
        """
        plaintext = plaintext.upper().replace(" ", "")
        ciphertext = ""
        for char in plaintext:
            row, col = self.find_in_table(char)
            adfgvx_char = self.adfgvx[row] + self.adfgvx[col]
            ciphertext += adfgvx_char
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypts the given ciphertext using the ADFGVX Cipher algorithm.

        Args:
            ciphertext (str): The ciphertext to be decrypted.

        Returns:
            str: The plaintext generated from the ciphertext.
        """
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            adfgvx_char = ciphertext[i:i+2]
            row = self.adfgvx.index(adfgvx_char[0])
            col = self.adfgvx.index(adfgvx_char[1])
            plaintext += self.substitution_table[row][col]
        return plaintext

    def find_in_table(self, char):
        """
        Finds the position of a given character in the substitution table.

        Args:
            char (str): The character to be found in the substitution table.

        Returns:
            Tuple[int, int]: A tuple containing the row and column position of the character in the substitution table.
        """
        for row in range(6):
            for col in range(6):
                if self.substitution_table[row][col] == char:
                    return row, col

