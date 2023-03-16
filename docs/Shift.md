# Shift Cipher

The shift cipher, also known as the Caesar cipher, is a simple encryption technique that involves shifting the letters of a message by a certain number of positions in the alphabet. The shift value is a key that is used for both encryption and decryption.

## Encryption
The encryption process for a shift cipher can be represented by the following formula:

$$E(x) = (x + k) \mod 26$$
where:
- $E(x)$ is the encrypted letter.
- $x$ is the plaintext letter, represented as a number between 0 and 25. (i.e: A=0, B=1, C=2, ..., z=25)
- $k$ is the shift value, represented as a number between 0 and 25.

To encrypt a message, each letter in the plaintext is shifted by the same amount specified by the shift value. For example, if the shift value is 3, then the letter 'A' becomes 'D', 'B' becomes 'E', and so on.

## Decryption
The decryption process for a shift cipher can be represented by the following formula:

$$D(x) = (x - k) \mod 26$$
where:
- $D(x)$ is the decrypted letter.
- $x$ is the encrypted letter, represented as a number between 0 and 25.
- $k$ is the shift value, represented as a number between 0 and 25

To decrypt a message, each letter in the encrypted message is shifted back by the same amount specified by the shift value. For example, if the shift value is 3, then the letter 'D' becomes 'A', 'E' becomes 'B', and so on.

**Note** : the shift value is the same for both encryption and decryption. If the shift value is known to an attacker, then the encryption can be easily broken by trying all possible shift values until the correct one is found. Therefore, the shift cipher is not recommended for secure communication, but can be useful for basic encryption needs or educational purposes.

## Implementation
The implementation of the ShiftCipher class is based on the following steps:

1. Initialize the shift value during class instantiation.

2. Define the `encrypt` method that takes a message as a parameter and returns the encrypted message.

3. Iterate over each character in the message and check if it is an alphabetic character.
4. If the character is alphabetic, shift it by the shift value and add it to the encrypted message.
5. If the character is not alphabetic, add it to the encrypted message as is.
6. Define the `decrypt` method that takes an encrypted message as a parameter and returns the original message.
7. Iterate over each character in the encrypted message and check if it is an alphabetic character.
8. If the character is alphabetic, shift it back by the shift value and add it to the decrypted message.
9. If the character is not alphabetic, add it to the decrypted message as is.
10. Return the encrypted or decrypted message as a string.


## Usage
To use the ShiftCipher class in Python, first import the class into your code:

```python
from Shift import ShiftCipher
```

Then, create an instance of the ShiftCipher class with a shift value:

```python
cipher = ShiftCipher(3)
```

To encrypt a message, call the `encrypt` method with the message as a parameter:

```python
encrypted_message = cipher.encrypt("HELLO")
```

To decrypt an encrypted message, call the `decrypt` method with the encrypted message as a parameter:

```python
decrypted_message = cipher.decrypt("KHOOR")
```

## Example
Here's an example of how to use the ShiftCipher class to encrypt and decrypt a message:

```python
from Shift import ShiftCipher

cipher = ShiftCipher(3)
message = "Hello, World!"
encrypted_message = cipher.encrypt(message)
decrypted_message = cipher.decrypt(encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
```

Output:

```yaml
Original message: Hello, World!
Encrypted message: Khoor, Zruog!
Decrypted message: Hello, World!
```

## Limitations
The shift cipher is a very simple encryption technique and has some limitations. For example, it can be easily broken by brute force or frequency analysis attacks. Additionally, the shift value is a weak key that can be easily guessed or discovered through trial and error. Therefore, the shift cipher is not recommended for secure communication, but can be useful for basic encryption needs or educational purposes.
