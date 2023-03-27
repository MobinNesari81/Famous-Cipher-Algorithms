# Rail Fence Cipher
__Designer and Developer:__ Mobin Nesari

The Rail Fence Cipher is a transposition cipher that encrypts plaintext by writing it diagonally on a set number of rails, and then reading off the ciphertext from the rows.

## How It Works?
To encrypt a message using the Rail Fence Cipher, follow these steps:

- Write the message out in a diagonal pattern on a set number of rails.
- Read off the ciphertext from each row, starting from the top left and working down to the bottom right.

For example, suppose we want to encrypt the message "HELLO WORLD!" using the Rail Fence Cipher with three rails. We would first write the message out in a diagonal pattern on three rails like so:

```
H . . . O . . . L . .
. E . L . W . R . D .
. . L . . . O . . . !
```

Then we would read off the ciphertext from each row, starting from the top left and working down to the bottom right:

```
HOLELWRDLO!!
```

To decrypt a message using the Rail Fence Cipher, simply reverse the process:

1. Calculate the length of the ciphertext and divide it by the number of rails to get the length of each row.
2. Create an empty grid with the correct number of rows and columns.
3. Fill in the grid with asterisks where the ciphertext letters will go.
4. Write the ciphertext into the grid in a diagonal pattern.
5. Read off the plaintext from the grid by following the same diagonal pattern.

## Strengths and Weaknesses
The Rail Fence Cipher is fairly simple and easy to implement, but it is not very secure. It can be easily broken using frequency analysis or other common cryptanalysis techniques. However, it can be useful as a basic way to obscure a message from casual observers.

## Usage
The `RailFenceCipher` class in this module can be used to encrypt and decrypt messages using the Rail Fence Cipher. To use it, simply create a new instance of the class with a key specifying the number of rails to use, and then call the `encrypt()` or `decrypt()` method with the plaintext or ciphertext respectively.

```python
import FamousCipherAlgorithms
RFC = FCA.RailFenceCipher(3)
plaintext = "HELLO WORLD"
ciphertext = RFC.encrypt(plaintext)
decrypted_plaintext = RFC.decrypt(ciphertext)

print("Plaintext:      ", plaintext)
print("Ciphertext:     ", ciphertext)
print("Decrypted text: ", decrypted_plaintext)
```

This will output:

```
Plaintext:       HELLO WORLD
Ciphertext:      HOREL OLLWD
Decrypted text:  HELLO WORLD
```

## References
- <a href="https://en.wikipedia.org/wiki/Rail_fence_cipher"> Wikipedia: Rail fence cipher</a>
