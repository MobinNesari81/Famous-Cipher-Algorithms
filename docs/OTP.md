<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>

# One Time Pad (Vernam) Cipher

The One Time Pad Cipher is a cryptographic algorithm that uses a random key and a mathematical operation to encrypt plaintext. It is considered to be one of the most secure encryption methods, as it is impossible to crack if used correctly.

## Encryption Process
To encrypt a message using the One Time Pad Cipher, follow these steps:

1. Generate a random key that is at least as long as the plaintext message.
2. Convert the plaintext message into a series of numbers or letters (depending on the encoding method used).
3. Use modular addition (or subtraction) to combine each number in the plaintext message with the corresponding number in the key. If the result is greater than the maximum value allowed by the numbering system being used, wrap around to the beginning.
4. Convert the resulting series of numbers back into letters, if necessary.

## Decryption Process
To decrypt a message that has been encrypted using the One Time Pad Cipher, the recipient must have access to the key that was used for encryption. To decrypt the message, follow these steps:

1. Convert the encrypted message into a series of numbers or letters (depending on the encoding method used).
2. Use modular subtraction (or addition) to subtract each number in the encrypted message from the corresponding number in the key. If the result is negative, add the maximum value allowed by the numbering system being used.
3. Convert the resulting series of numbers back into letters, if necessary.

## Example
Suppose we want to encrypt the following message using the One Time Pad Cipher:

```
PLAINTEXT: HELLO
```

We generate a random key that is at least as long as the plaintext message:

```
KEY: LXFOPVEFRNHR
```

We convert the plaintext message into a series of numbers using the ASCII encoding method:

```
PLAINTEXT: H    E    L    L    O
ASCII:     72   69   76   76   79
```

We use modular addition to combine each number in the plaintext message with the corresponding number in the key:

```
PLAINTEXT: H    E    L    L    O
ASCII:     72   69   76   76   79
KEY:       L    X    F    O    P
ASCII:     76   88   70   79   80
CIPHER:    P    B    V    R    T
```

The resulting ciphertext is `PBVRT`.

To decrypt the message, we need the key that was used for encryption:

```
KEY:      LXFOPVEFRNHR
```

We convert the ciphertext into a series of numbers using the ASCII encoding method:

```
CIPHER:    P    B    V    R    T
ASCII:     80   66   86   82   84
```

We use modular subtraction to subtract each number in the ciphertext from the corresponding number in the key:

```
CIPHER:    P    B    V    R    T
ASCII:     80   66   86   82   84
KEY:       L    X    F    O    P
ASCII:     76   88   70   79   80
PLAINTEXT: H    E    L    L    O
```

The resulting plaintext is `HELLO`.

## Strengths and Weaknesses
One-time pad cipher algorithm is known for its strength in terms of providing perfect secrecy, making it virtually impossible to crack the encrypted message without having access to the secret key. The algorithm uses a random key that is as long as the plaintext, which means that the ciphertext provides no information about the original message unless the key is known. However, the main weakness of the one-time pad cipher algorithm lies in the distribution and management of the secret key. The key must be shared securely between the sender and the recipient, and it can only be used once. Also, generating truly random keys can be challenging, and any errors in the key can lead to incorrect decryption of the message. Additionally, the key must be kept secure at all times, otherwise, anyone who gets hold of it can easily decrypt the messages.

## Usage
The `OneTimePad` class in this module can be used to encrypt and decrypt messages using the One-Time Pad Cipher. To use it, simply create a new instance of the class and an auto generated key, and then call the `encrypt()` or `decrypt()` method with the plaintext or ciphertext respectively.

```python
import FamousCipherAlgorithms as FCA
message = "HELLO WORLD"
cipher = OneTimePad(message)

# Encrypt the message
encrypted_message = cipher.encrypt()
print("Encrypted Message:", encrypted_message)

# Generated key
print("Key:", cipher.key)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)
```

The result will be something similar to :

```
Encrypted Message: RWASDPHNPO
Key: KSPHPTTWEL
Decrypted Message: HELLOWORLD
```

## References
- <a href="https://en.wikipedia.org/wiki/One-time_pad"> Wikipedia: One-time pad</a>