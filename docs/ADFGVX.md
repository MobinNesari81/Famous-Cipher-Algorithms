<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>

# ADFGVX Cipher


The ADFGVX cipher is a cryptographic cipher that was used by the German Army in World War I. It is a fractionating transposition cipher that uses a combination of a Polybius square and a columnar transposition to encrypt messages.

The name "ADFGVX" comes from the fact that the cipher only uses six symbols: A, D, F, G, V, and X. These symbols were chosen because they are easy to transmit using Morse code.

## Encryption Process
The encryption process of the ADFGVX cipher can be summarized in three steps:

1. Generate a substitution table using a keyword.
2. Convert each character of the plaintext into its corresponding ADFGVX symbol using the substitution table.
3. Concatenate the resulting symbols to form the ciphertext.

## Substitution Table
The substitution table is a 6x6 grid that contains all the letters and digits of the alphabet, plus the six ADFGVX symbols. To generate the substitution table, a keyword is used as follows:

1. Remove duplicates from the keyword.
2. Sort the unique characters of the keyword alphabetically.
3. Fill the first row of the substitution table with the sorted keyword.
4. Fill the remaining cells of the table with the remaining letters and digits of the alphabet in a random order.

## Conversion to ADFGVX Symbols
Each character of the plaintext is then converted into its corresponding ADFGVX symbol using the substitution table. To find the ADFGVX symbol for a given character, we need to find its position in the substitution table, and use the row and column indexes as the two components of the ADFGVX symbol.

For instance, if the substitution table is 

<div align="center">

| K | L | M | N | O | P |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q | R | S | T | U | V |
| W | X | Y | Z | 0 | 1 |
| 2 | 3 | 4 | 5 | 6 | 7 |
| 8 | 9 | A | B | C | D |
| E | F | G | H | I | J |

</div>

And we want to encrypt the message "HELLO", we would first convert each character into its corresponding row and column indexes:

```
H -> (1, 4)
E -> (0, 5)
L -> (0, 1)
L -> (0, 1)
O -> (0, 3)
```

And then concatenate the resulting ADFGVX symbols to obtain the ciphertext:

```
DG FF GD GG FX XD AG DD GF FA
```

## Decryption Process
The decryption process of the ADFGVX cipher is simply the reverse of the encryption process:

1. Use the same keyword to generate the substitution table.
2. Convert pairs of ADFGVX symbols back into plain characters using the substitution table.

For example, if we have the ciphertext "DGFFGDGGFXXDAGDDGFFA" and the same substitution table as before, we would first split the ciphertext into pairs of ADFGVX symbols:

```
(1, 4) -> H
(0, 5) -> E
(0, 1) -> L
(0, 1) -> L
(0, 3) -> O
```
Concatenating these characters gives us the original plaintext: "HELLO".

## Usage
The `ADFGVXCipher` class in this module can be used to encrypt and decrypt messages using the Polybius Square Cipher. To use it, simply create a new instance of the class with a key, and then call the `encrypt()` or `decrypt()` method with the plaintext or ciphertext respectively.

```python
import FamousCipherAlgorithms as FCA
cipher = FCA.ADFGVXCipher("SECRET")
text = "HELLO WORLD"
ciphertext = cipher.encrypt(text)
decryptedtext = cipher.decrypt(ciphertext)

print(f'Plain Text: {text}')
print(f'Cipher Text: {ciphertext}')
print(f'Decrypted Text: {decryptedtext}')
```

The result will be:

```
Plain Text: HELLO WORLD
Cipher Text: AXADGGGGVFVXVFAFGGFF
Decrypted Text: HELLOWORLD
```

## References
- <a href="https://en.wikipedia.org/wiki/ADFGVX_cipher"> Wikipedia: ADFGVX Cipher</a>