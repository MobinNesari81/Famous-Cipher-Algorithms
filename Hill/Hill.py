import numpy as np

class HillCipher:
    """
    A class that implements the Hill Cipher encryption and decryption algorithm using numpy.
    
    Attributes:
        key (numpy.ndarray): A square matrix of size n x n where n is the length of the key.
        n (int): The length of the key matrix.
        modulus (int): The modulus used for the encryption and decryption. Default is 26 for English alphabet.
    
    Methods:
        encrypt(plaintext: str) -> str:
            Encrypts a plaintext message using the Hill Cipher algorithm.
            Returns the ciphertext message.
        
        decrypt(ciphertext: str) -> str:
            Decrypts a ciphertext message using the Hill Cipher algorithm.
            Returns the plaintext message.
    """
    def __init__(self, key):
        """
        Initializes the HillCipher object.
        
        Args:
            key (list): A list of lists representing the key matrix.
                        The key matrix should be a square matrix of size n x n where n is the length of the key.
        """
        self.key = np.array(key) # key is a square matrix of size n x n where n is the length of the key
        self.n = len(key)
        self.modulus = 26 # we're working with mod 26 arithmetic for the English alphabet
    
    def encrypt(self, plaintext):
        """
        Encrypts a plaintext message using the Hill Cipher algorithm.
        
        Args:
            plaintext (str): The plaintext message to encrypt.
        
        Returns:
            str: The ciphertext message.
        """
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.upper()
        # pad the plaintext with 'X' if its length is not divisible by n
        if len(plaintext) % self.n != 0:
            plaintext += 'X' * (self.n - len(plaintext) % self.n)
        
        start_idx = ord('A')
        
        # split the plaintext into blocks of length n
        plaintext_blocks = [plaintext[i:i+self.n] for i in range(0, len(plaintext), self.n)]
        
        # encrypt each block of plaintext using the key matrix
        ciphertext_letters = []
        ciphertext_blocks = []
        for block in plaintext_blocks:
            block_matrix = np.array([ord(char) - ord('A') for char in block]).reshape(-1, 1)
            ciphertext_matrix = (self.key @ block_matrix) % self.modulus
            for num in ciphertext_matrix.flatten():
                ciphertext_letters.append(chr(num + start_idx))
        
        # concatenate the encrypted blocks and return the ciphertext
        ciphertext = ''.join(ciphertext_letters)
        return ciphertext
    
    def decrypt(self, ciphertext):
        """
        Decrypts a ciphertext message using the Hill Cipher algorithm.
        
        Args:
            ciphertext (str): The ciphertext message to decrypt.
        
        Returns:
            str: The plaintext message.
        """
        ciphertext = ciphertext.upper()
        # split the ciphertext into blocks of length n
        ciphertext_blocks = [ciphertext[i:i+self.n] for i in range(0, len(ciphertext), self.n)]
        # compute the inverse of the key matrix
        key_inv = np.linalg.inv(self.key)
        key_det = round(np.linalg.det(self.key)) % self.modulus
        key_adj = np.round(key_det * key_inv) % self.modulus
        key_inv = key_adj.astype(int)
        
        # decrypt each block of ciphertext using the inverse of the key matrix
        plaintext_blocks = []
        for block in ciphertext_blocks:
            block_matrix = np.array([ord(char) - ord('A') for char in block]).reshape(-1, 1)
            plaintext_matrix = (key_inv @ block_matrix) % self.modulus
            for num in plaintext_matrix.flatten():
                plaintext_blocks.append(chr(num + ord('A')))
        
        
        # concatenate the decrypted blocks and return the plaintext
        plaintext = ''.join(plaintext_blocks)
        return plaintext


if __name__ == '__main__':
    key = [[2, 1], [1, 1]]
    cipher = HillCipher(key)
    plaintext = 'HELLO WORLD'
    ciphertext = cipher.encrypt(plaintext)
    print(ciphertext) # prints 'CFKMU'
    decrypted_plaintext = cipher.decrypt(ciphertext)
    print(decrypted_plaintext) # prints 'HELLO'