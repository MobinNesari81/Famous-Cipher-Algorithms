# Hill Cipher
The Hill Cipher is a symmetric key encryption algorithm that operates on blocks of plaintext. It was invented by Lester S. Hill in 1929 and is based on linear algebra. The Hill Cipher uses a key matrix, which is a square matrix of size n x n, where n is the length of the key. The plaintext is divided into blocks of n characters and each block is encrypted using the key matrix.

## How It Works?

### Key Generation
The Hill Cipher key is a square matrix of size n x n. The elements of the key matrix are chosen from a set of integers mod 26, which corresponds to the English alphabet. The key matrix must be invertible mod 26 in order for the cipher to work correctly. The determinant of the key matrix must also be relatively prime to 26.

### Encryption
The plaintext is divided into blocks of n characters. If the length of the plaintext is not divisible by n, the plaintext is padded with 'X' characters. Each block of plaintext is then converted to a column vector and multiplied by the key matrix mod 26. The resulting column vector is then converted back to a string of characters.

### Decryption
The ciphertext is divided into blocks of n characters. Each block of ciphertext is then converted to a column vector and multiplied by the inverse of the key matrix mod 26. The resulting column vector is then converted back to a string of characters.

## HillCipher Class
The `HillCipher` class is a Python implementation of the Hill Cipher algorithm using the NumPy library. The class takes a key matrix as input and provides methods for encryption and decryption of messages.

### Usage
To use the `HillCipher` class, create an instance of the class with a key matrix as input. The key matrix must be a 2-dimensional list or array of integers.

```python
import numpy as np
from hill_cipher import HillCipher

# create key matrix
key = [[2, 1], [1, 1]]

# create HillCipher instance
cipher = HillCipher(key)
```

To encrypt a message, call the `encrypt` method of the `HillCipher` instance with the plaintext as input.

```python
# encrypt plaintext
plaintext = 'HELLO'
ciphertext = cipher.encrypt(plaintext)

print(ciphertext) # prints 'CFKMU'
```

To decrypt a message, call the `decrypt` method of the `HillCipher` instance with the ciphertext as input.

```python
# decrypt ciphertext
decrypted_plaintext = cipher.decrypt(ciphertext)

print(decrypted_plaintext) # prints 'HELLO'
```

### Example
```python
import numpy as np
from hill_cipher import HillCipher

# create key matrix
key = [[2, 1], [1, 1]]

# create HillCipher instance
cipher = HillCipher(key)

# encrypt plaintext
plaintext = 'HELLO'
ciphertext = cipher.encrypt(plaintext)

print(ciphertext) # prints 'CFKMU'

# decrypt ciphertext
decrypted_plaintext = cipher.decrypt(ciphertext)

print(decrypted_plaintext) # prints 'HELLO'
```
