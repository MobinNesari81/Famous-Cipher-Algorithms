class RailFenceCipher:
    """
    A class that implements the rail fence cipher encryption and decryption.
    """
    def __init__(self, key: int):
        """
        Initializes an instance of the RailFenceCipher class.

        Args:
            key (int): The number of rails to be used in the encryption/decryption process.
        """
        self.key = key
        
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a given plaintext using the rail fence cipher algorithm.

        Args:
            plaintext (str): The plaintext to be encrypted.

        Returns:
            str: The encrypted ciphertext.
        """
        rail = [['\n' for i in range(len(plaintext))]
                  for j in range(self.key)]
        
        dir_down = False
        row, col = 0, 0

        for i in range(len(plaintext)):
            if (row == 0) or (row == self.key - 1):
                dir_down = not dir_down

            rail[row][col] = plaintext[i]
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
                
        ciphertext = ""
        for i in range(self.key):
            for j in range(len(plaintext)):
                if rail[i][j] != '\n':
                    ciphertext += rail[i][j]
                    
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a given ciphertext using the rail fence cipher algorithm.

        Args:
            ciphertext (str): The ciphertext to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        rail = [['\n' for i in range(len(ciphertext))]
                  for j in range(self.key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(self.key):
            for j in range(len(ciphertext)):
                if ((rail[i][j] == '*') and (index < len(ciphertext))):
                    rail[i][j] = ciphertext[index]
                    index += 1

        plaintext = ""
        row, col = 0, 0
        for i in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key-1:
                dir_down = False

            if rail[row][col] != '*':
                plaintext += rail[row][col]
                col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        return plaintext
