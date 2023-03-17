# Permutation Cipher

The permutation cipher is a type of encryption technique that operates by permuting the order of the plaintext characters to generate ciphertext. In other words, the permutation cipher encrypts a message by rearranging the order of the characters in the plaintext according to a predefined sequence. The security of this technique depends on the complexity of the permutation sequence used.

The permutation cipher can be implemented using a variety of methods, including using a random sequence, a pre-determined sequence, or a secret key. In a pre-determined permutation sequence, the order of the characters is predetermined and is known by both the sender and receiver. The sender uses this sequence to encrypt the plaintext message, while the receiver uses it to decrypt the ciphertext message.

For an arbitrary key (i.e., a permutation) $\pi$, we define:

$$e_\pi(x_1, \dots, x_m) = (x_{\pi(1)}, \dots, x_{\pi(m)})$$

$$d_\pi(y_1, \dots, y_m) = (y_{\pi^{-1}(1)}, \dots, y_{\pi^{-1}(m)})$$


## Description
The `PermutationCipher` class in this code implements the permutation cipher. It takes a list of integers as a key to define the permutation. The key should contain unique integers ranging from 0 to the length of the plaintext. The `permute()` method takes a section of plaintext and applies the permutation defined by the key to rearrange the characters. The `inv_permute()` method takes a section of ciphertext and applies the inverse permutation to recover the original plaintext. The `encrypt()` method takes a plaintext message and applies the permutation cipher to encrypt it. The `decrypt()` method takes a ciphertext message and applies the inverse permutation to decrypt it.

## Implementation
The provided code implements the permutation cipher using a pre-determined sequence, which is passed to the `PermutationCipher` class as a list of integers. The class has the following methods:

- `__init__(self, key: list)` - Initializes the `PermutationCipher` class with the provided key sequence.

- `permute(self, section: str) -> str` - Permutes the characters in the given section of plaintext.
- `inv_permute(self, section: str) -> str` - Inverse permutes the characters in the given section of ciphertext.
- `encrypt(self, plaintext: str) -> str` - Encrypts the given plaintext using the permutation cipher.
- `decrypt(self, cipher_text: str) -> str` - Decrypts the given ciphertext using the permutation cipher.

The `permute` method takes a plaintext section and returns a ciphertext section by permuting the characters according to the key sequence. The `inv_permute` method takes a ciphertext section and returns the corresponding plaintext section by performing the inverse permutation. The `encrypt` method takes a plaintext message and returns the corresponding ciphertext message by applying `permute` to each plaintext section. The `decrypt` method takes a ciphertext message and returns the corresponding plaintext message by applying `inv_permute` to each ciphertext section.

To use the provided code, create an instance of the `PermutationCipher` class with a key sequence as a list of integers. You can then call the `encrypt` method with a plaintext message to get the corresponding ciphertext message, or call the `decrypt` method with a ciphertext message to get the corresponding plaintext message.

Note that the provided code assumes that the plaintext message consists only of uppercase letters and spaces. If you want to use the code to encrypt messages with other characters, you will need to modify it accordingly.

## Usage

To use the `PermutationCipher` class, simply create an instance of the class with a key that defines the permutation to use. Then call the `encrypt()` method with the plaintext message to encrypt it, or call the `decrypt()` method with the ciphertext message to decrypt it.

For example:

```python
key = [2, 1, 4, 0, 3]  # Define a key to use for the permutation cipher
cipher = PermutationCipher(key)  # Create an instance of the PermutationCipher class
plaintext = "Hello World!"  # Define a plaintext message to encrypt
ciphertext = cipher.encrypt(plaintext)  # Encrypt the plaintext message
print(ciphertext)  # Print the ciphertext message
decrypted_text = cipher.decrypt(ciphertext)  # Decrypt the ciphertext message
print(decrypted_text)  # Print the decrypted plaintext message
```

This will output:

```
LEOHLRODWLXXX!X 
HELLOWORLD!
```
