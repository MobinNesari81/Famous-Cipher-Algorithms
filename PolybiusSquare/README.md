# Polybius Square Cipher
__Design and Develop:__ Mobin Nesari

The Polybius Square Cipher is a simple substitution cipher that encrypts pairs of letters instead of individual ones. It derives its name from the Greek historian Polybius who used a similar method to encode messages.

## Encryption
To encrypt a message using the Polybius Square Cipher, follow these steps:

1. Create a 5x5 grid with the letters A through Z (excluding J) arranged in order. The first row should be filled with the letters A through E, the second row with F through J, and so on until the fifth row which should be filled with V through Z.

2. Divide the plaintext into pairs of letters. If there is an odd number of letters, append a letter (e.g., X) to make it even.

3. For each pair of letters, find the row and column in the grid corresponding to the first and second letter, respectively. Concatenate these numbers to form a two-digit number representing the position of the pair.

4. Repeat step 3 for each pair of letters in the plaintext.

5. The encrypted message consists of the two-digit numbers separated by spaces.

For example, suppose we want to encrypt the message "HELLO WORLD". We would first create the following grid:

<div align="center">

|   | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|---|---|
| 1 | A | B | C | D | E |
| 2 | F | G | H | I | K |
| 3 | L | M | N | O | P |
| 4 | Q | R | S | T | U |
| 5 | V | W | X | Y | Z |
</div>

We would then divide the plaintext into pairs of letters:
```
HE LL OW OR LD
```

And encrypt each pair by finding its position in the grid:

```
23 32 34 44 31 24
```

So the encrypted message would be:

```
23 32 34 44 31 24
```

## Decryption
To decrypt a message encrypted with the Polybius Square Cipher, follow these steps:

1. Create the same 5x5 grid used for encryption.

2. Divide the ciphertext into pairs of two-digit numbers.

3. For each pair of numbers, use the row and column to find the corresponding letter in the grid.

4. Concatenate the letters to form the decrypted message.

For example, suppose we want to decrypt the message "23 32 34 44 31 24". We would first create the same grid used for encryption:

<div align="center">

|   | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|---|---|
| 1 | A | B | C | D | E |
| 2 | F | G | H | I | K |
| 3 | L | M | N | O | P |
| 4 | Q | R | S | T | U |
| 5 | V | W | X | Y | Z |
</div>

We would then divide the ciphertext into pairs:
```
23 32 34 44 31 24
```

And decrypt each pair by finding the corresponding letter in the grid:

```
HE LL OW OR LD
```

So the decrypted message would be:

```
HELLOWORLD
```

## Strengths and Weaknesses
The Polybius Square Cipher is a substitution cipher that replaces each letter with a pair of numbers representing its row and column in a predetermined grid. Its strength lies in the fact that it is more complex than a simple Caesar cipher and can withstand frequency analysis attacks. However, it has several weaknesses such as the limited number of characters that can be represented in the grid, making it vulnerable to brute force attacks, and the lack of a provision for key management, which makes it susceptible to known plaintext attacks. Additionally, if the grid is discovered, the cipher can be easily broken.

## Usage
The `PolybiusSquareCipher` class in this module can be used to encrypt and decrypt messages using the Polybius Square Cipher. To use it, simply create a new instance of the class with a key, and then call the `encrypt()` or `decrypt()` method with the plaintext or ciphertext respectively.

```python
import FamousCipherAlgorithms as FCA
PSC = PolybiusSquareCipher()
text = "I will see you at midnight"
enc = PSC.encrypt(text)
print(enc)
dec = PSC.decrypt(enc)
print(f" Text: {text}\n Ciphertext: {enc}\n Decrypted: {dec}")
```
The result will be:
```
 Text: I will see you at midnight
 Ciphertext: 245224313143151554344511443224143324222344
 Decrypted: IWILLSEEYOUATMIDNIGHT
```

## References
- <a href="https://en.wikipedia.org/wiki/Polybius_square"> Wikipedia: Polybius Square</a>