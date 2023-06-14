
class ColumnarTranspositionCipher:
    def __init__(self, key: str) -> None:
        """
        Constructor method to initialize an instance of ColumnarTranspositionCipher with a key.

        Args:
        - key (str): A string representing the key used in the encryption and decryption processes.

        Returns:
        - None.
        """
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        """
        Method to encrypt plaintext using the Columnar Transposition Cipher algorithm.

        Args:
        - plaintext (str): A string representing the plaintext to be encrypted.

        Returns:
        - ciphertext (str): A string representing the encrypted ciphertext.
        """
        # remove spaces from plaintext and calculate length
        plaintext = plaintext.replace(" ", "")
        pt_len = len(plaintext)

        # calculate number of rows required using key length
        # and plaintext length
        key_len = len(self.key)
        num_rows = pt_len // key_len
        if pt_len % key_len != 0:
            num_rows += 1

        # pad plaintext with 'X' to fill last row
        padding_len = num_rows * key_len - pt_len
        plaintext += "X" * padding_len

        # create list of columns
        cols = []
        for i in range(key_len):
            col = ""
            for j in range(num_rows):
                col += plaintext[j * key_len + i]
            cols.append(col)

        # sort columns according to key
        sorted_cols = [cols[self.key.index(str(i + 1))] for i in range(key_len)]

        # concatenate columns to form ciphertext
        ciphertext = "".join(sorted_cols)

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Method to decrypt ciphertext using the Columnar Transposition Cipher algorithm.

        Args:
        - ciphertext (str): A string representing the ciphertext to be decrypted.

        Returns:
        - plaintext (str): A string representing the decrypted plaintext.
        """
        # calculate number of rows required using key length
        # and ciphertext length
        ct_len = len(ciphertext)
        key_len = len(self.key)
        num_rows = ct_len // key_len
        
        # create empty matrix to hold ciphertext characters
        matrix = []
        for i in range(num_rows):
            row = [""] * key_len
            matrix.append(row)

        # populate matrix with ciphertext characters
        index = 0
        for i in range(key_len):
            col_index = self.key.index(str(i + 1))
            for j in range(num_rows):
                matrix[j][col_index] = ciphertext[index]
                index += 1

        # concatenate matrix rows to form plaintext
        plaintext = ""
        for i in range(num_rows):
            for j in range(key_len):
                plaintext += matrix[i][j]

        # remove padding 'X' characters from plaintext
        plaintext = plaintext.replace("X", "")

        return plaintext
    