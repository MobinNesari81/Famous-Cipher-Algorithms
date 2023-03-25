class AffineCipher:
    def __init__(self, a, b):
        if not are_coprime(a, 26): # Check a is invertible
            raise Exception("Coefficient a should be co-prime with 26!")
        self.a = a
        self.b = b
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, message):
        """Encrypts a message using the Affine cipher."""
        cipher_text = ''
        for char in message.lower():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                # Apply the Affine transformation
                new_index = (self.a * index + self.b) % 26
                cipher_text += self.alphabet[new_index]
            else:
                cipher_text += char
        return cipher_text

    def decrypt(self, cipher_text):
        """Decrypts a message encrypted with the Affine cipher."""
        plaintext = ''
        for char in cipher_text.lower():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                # Inverse Affine transformation
                new_index = (self.modular_inverse(self.a, 26) * (index - self.b)) % 26
                plaintext += self.alphabet[new_index]
            else:
                plaintext += char
        return plaintext

    def modular_inverse(self, a, m):
        """Calculates the modular inverse of a with respect to m."""
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

def gcd(a, b):
    """Calculates the greatest common divisor of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    """Determines whether two numbers are coprime or not."""
    return gcd(a, b) == 1

