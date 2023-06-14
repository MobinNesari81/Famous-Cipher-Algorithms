
import re


class BeaufortCipher:
    """
       Initializes a Beaufort Cipher object with the given key.
       :param key: A string representing the key to use for the cipher.
       :type key: str
       :raises Exception: If the key contains any non-letter character.
    """

    ALPHABET_SIZE = 26

    def __init__(self, key: str) -> None:
        self._key = key.lower()
        self._key_array = []
        self.set_key(self._key)

    def get_key(self) -> str:
        """
        Returns:
        A String representing the key.
        """
        return self._key.upper()

    def set_key(self, key: str) -> None:
        """
        Takes a string and sets it as key.

        Arguments:
        key -- string representing the key.
        """
        if self.is_key_valid(key.lower()):
            self._key_array = [ord(letter) - ord('a') for letter in self._key]  # the ascii number of a is ord('a')=97
        else:
            raise Exception("Invalid Key")

    @staticmethod
    def is_key_valid(key: str) -> bool:
        """
        Takes a string representing the key and verifies it for the Beaufort Cipher.

        Arguments:
        key -- string representing the key.

        Returns:
        A Boolean representing the key's validity.
        """

        return re.match("^[a-z]+$", key) is not None

    def encrypt(self, plaintext: str) -> str:
        """
        Takes a string message and enciphers it using the Beaufort cipher.

        Arguments:
        ciphertext -- a string message to be enciphered.

        Returns:
        A string representing the ciphered message.
        """

        plaintext = plaintext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)
        ciphertext = ""

        i = 0
        for letter in plaintext:
            letter_num = ord(letter) - ord('a')
            cipher_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            ciphertext += chr(cipher_letter_num + ord('a'))

            i = (i+1) % len(self._key)

        return ciphertext.upper()

    def decrypt(self, ciphertext: str) -> str:
        """
        Takes a string message and deciphers it using the Beaufort cipher.

        Arguments:
        ciphertext -- a string message to be deciphered.

        Returns:
        A string representing the deciphered message.
        """

        ciphertext = ciphertext.lower()
        ciphertext = re.sub("[^a-z]+", "", ciphertext)
        plaintext = ""

        i = 0
        for letter in ciphertext:
            letter_num = ord(letter) - ord('a')
            plain_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            plaintext += chr(plain_letter_num + ord('a'))

            i = (i + 1) % len(self._key)

        return plaintext
