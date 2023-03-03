class ShiftCipher:
    """
    A class that implements a shift cipher for encrypting and decrypting messages.

    Attributes:
    -----------
    shift : int
        The shift value to use for encrypting and decrypting messages. The value must be an integer between 0 and 25.

    Methods:
    --------
    encrypt(message: str) -> str:
        Encrypts the given message using the shift value and returns the encrypted message as a string.

    decrypt(message: str) -> str:
        Decrypts the given encrypted message using the shift value and returns the original message as a string.

    """

    def __init__(self, shift: int):
        """
        Initializes a new instance of the ShiftCipher class with the given shift value.

        Parameters:
        -----------
        shift : int
            The shift value to use for encrypting and decrypting messages. The value must be an integer between 0 and 25.
        """
        self.shift = shift % 26

    def encrypt(self, message: str) -> str:
        """
        Encrypts the given message using the shift value and returns the encrypted message as a string.

        Parameters:
        -----------
        message : str
            The message to encrypt.

        Returns:
        --------
        str
            The encrypted message as a string.
        """
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char.upper()) - 65 + self.shift) % 26 + 65)
                encrypted_message += shifted_char if char.isupper() else shifted_char.lower()
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message: str) -> str:
        """
        Decrypts the given encrypted message using the shift value and returns the original message as a string.

        Parameters:
        -----------
        message : str
            The encrypted message to decrypt.

        Returns:
        --------
        str
            The original message as a string.
        """
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char.upper()) - 65 - self.shift) % 26 + 65)
                decrypted_message += shifted_char if char.isupper() else shifted_char.lower()
            else:
                decrypted_message += char
        return decrypted_message
