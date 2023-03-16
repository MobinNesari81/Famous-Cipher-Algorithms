# Vigenère Cipher

The Vigenère cipher is a polyalphabetic substitution cipher that was first described by Giovan Battista Bellaso in 1553. It was later misattributed to Blaise de Vigenère in the 19th century, which is where it gets its name. The Vigenère cipher is an extension of the Caesar cipher, and it is much more secure than the monoalphabetic substitution ciphers that were commonly used at the time.

## Explanation of the Vigenère Cipher
The Vigenère cipher uses a series of Caesar ciphers to encrypt a message. It uses a keyword or phrase to determine the shift for each letter in the plaintext message. The keyword is repeated as many times as necessary to match the length of the plaintext message.

To encrypt a message, we first generate a Vigenère table, which is a 26x26 matrix that contains all possible Caesar ciphers. The rows and columns of the table are labeled with the letters of the alphabet, and each cell in the table contains the letter that results from applying the Caesar cipher that corresponds to the row letter to the column letter.

To encrypt a letter of the plaintext message, we first determine the row of the Vigenère table that corresponds to the current letter of the keyword, and then we determine the column of the table that corresponds to the current letter of the plaintext message. The letter in the cell at the intersection of the row and column is the encrypted letter.

To decrypt a letter of the ciphertext message, we first determine the row of the Vigenère table that corresponds to the current letter of the keyword, and then we determine the column of the table that corresponds to the current letter of the ciphertext message. The letter in the row of the table that corresponds to the keyword letter and the column of the table that corresponds to the ciphertext letter is the decrypted letter.

## Usage
Here's an example of how to use the Vigenère cipher implementation provided:

```python
from vigenere_cipher import VigenereCipher

# Create a Vigenère cipher object with a key
cipher = VigenereCipher("KEY")

# Encrypt a message
plaintext = "HELLO"
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)  # outputs "RIJVS"

# Decrypt a message
decrypted_plaintext = cipher.decrypt(ciphertext)
print(decrypted_plaintext)  # outputs "HELLO"
```

First, we import the `VigenereCipher` class from the `vigenere_cipher` module. We then create a `VigenereCipher` object with a key of "KEY". We can then use the `encrypt()` method of the object to encrypt a plaintext message and the `decrypt()` method to decrypt a ciphertext message. In this example, we encrypt the plaintext message "HELLO" to produce the ciphertext message "RIJVS", and then decrypt the ciphertext message "RIJVS" to produce the original plaintext message "HELLO".
