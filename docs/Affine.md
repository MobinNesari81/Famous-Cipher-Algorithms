# Affine Cipher

The Affine cipher is a monoalphabetic substitution cipher that uses a simple mathematical function to encrypt a message. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. The Affine cipher is a special case of the more general monoalphabetic substitution cipher.

The encryption function is as follows:

$$E(x) = (ax + b)\text{mod}m$$

where x is the index of the plaintext letter in the alphabet, a and b are the key, and m is the size of the alphabet (26 for the English alphabet).

The decryption function is as follows:

$$D(x) = a^{-1}(x - b) \text{mod}m$$

## Implementation
The following Python code implements the Affine cipher:

```python
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

```

The AffineCipher class takes two arguments in its constructor: the key coefficients a and b. It checks if a is coprime with 26, and `raises an exception` if not.

The `encrypt` method takes a message string as input, and returns the corresponding ciphertext. It iterates through each character in the message, and applies the Affine transformation to each character.

The `decrypt` method takes a ciphertext string as input, and returns the corresponding plaintext. It iterates through each character in the ciphertext, and applies the inverse Affine transformation to each character.

The `modular_inverse` function calculates the modular inverse of a with respect to `m` using a brute-force method.

The `gcd` function calculates the greatest common divisor of two numbers `a` and `b`.

The `are_coprime` function decides whether two given numbers are coprime or not according to the result of the `gcd` function.

## How to Use Affine Cipher
Using the Affine Cipher in your own Python program is simple.

First, copy and paste the code for the `AffineCipher` class and the `gcd` and `are_coprime` helper functions into your program.

Next, create an instance of the `AffineCipher` class by passing in two integer values `a` and `b`.

- `a` should be a number that is coprime with 26. If `a` is not coprime with 26, an exception will be raised.
- `b` can be any integer value.

Here is an example of how to create an instance of the AffineCipher class:

```python
cipher = AffineCipher(3, 5)
```

Once you have created an instance of the `AffineCipher` class, you can use the `encrypt` and `decrypt` methods to encrypt and decrypt messages.

The `encrypt` method takes a plaintext message as a string and returns a ciphertext message as a string.

```python
plaintext = "hello world"
ciphertext = cipher.encrypt(plaintext)
print(ciphertext) # Output: 'dioxx wepnq'
```

The `decrypt` method takes a ciphertext message as a string and returns the original plaintext message as a string.

```python
ciphertext = "dioxx wepnq"
plaintext = cipher.decrypt(ciphertext)
print(plaintext) # Output: 'hello world'
```
