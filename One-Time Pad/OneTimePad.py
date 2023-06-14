
import random


class OneTimePad:
    def __init__(self, message: str) -> None:
        message = message.replace(' ', '')
        self.message = message.upper()
        self.key = self.generate_key(len(message))

    def generate_key(self, length: int) -> str:
        """Generate a random key of the same length as the message"""
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

    def encrypt(self) -> str:
        """Encrypt the message using the one-time pad cipher"""
        encrypted_text = ''
        for i in range(len(self.message)):
            # Convert the letters to ASCII values and XOR them with the corresponding key character
            encrypted_char = chr(((ord(self.message[i]) - ord('A')) + (ord(self.key[i]) - ord('A'))) % 26 + ord('A'))
            encrypted_text += encrypted_char
        return encrypted_text

    def decrypt(self, encrypted_message):
        """Decrypt the message using the one-time pad cipher"""
        decrypted_text = ''
        for i in range(len(encrypted_message)):
            # XOR the encrypted character with the corresponding key character to get back the original letter
            decrypted_char = chr(((ord(encrypted_message[i]) - ord('A')) - (ord(self.key[i]) - ord('A'))) % 26 + ord('A'))
            decrypted_text += decrypted_char
        return decrypted_text
