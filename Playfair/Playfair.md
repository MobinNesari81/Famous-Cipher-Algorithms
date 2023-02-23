# Playfair Cipher

The Playfair Cipher is a polygraphic substitution cipher that encrypts pairs of letters, known as bigrams, instead of single letters, unlike traditional substitution ciphers. This cipher was used extensively in the Second Boer War and both World War I and World War II.

## What is the Playfair Cipher?
The Playfair cipher is a cryptographic technique that was invented by Sir Charles Wheatstone in 1854. It uses a 5x5 grid of letters to encode a message. The grid is filled with a keyword, and then the remaining letters of the alphabet are added in order, skipping any letters that appear in the keyword. The resulting grid is used to encode and decode messages.

The Playfair cipher is a polygraphic substitution cipher, meaning that it encrypts multiple letters at once. Specifically, it encrypts pairs of letters (called digraphs) instead of individual letters. This makes it more secure than simple substitution ciphers, which only encrypt individual letters.

## How does the Playfair Cipher work?

The Playfair cipher uses a 5x5 grid of letters to encrypt messages. To create the grid, a keyword is first chosen. The keyword is then used to fill in the first row of the grid, with any repeated letters removed. The remaining letters of the alphabet are then added to the grid in order, skipping any letters that appear in the keyword. Here is an example of a Playfair cipher grid:

```
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z
```
To encrypt a message using the Playfair cipher, the message is split into pairs of letters (digraphs). If the message contains an odd number of letters, a dummy letter (such as "X") is added to the end to make it even. For each pair of letters, the following steps are performed:

1. If both letters are the same, add a dummy letter (such as "X") after the first letter.

2. Find the positions of the two letters in the Playfair cipher grid.

3. If the letters are in the same row of the grid, replace them with the letters to their right, wrapping around to the beginning of the row if necessary.

4. If the letters are in the same column of the grid, replace them with the letters below them, wrapping around to the top of the column if necessary.

5. If the letters are in different rows and columns, replace them with the letters in the same row but in the column of the other letter.

For example, suppose we want to encrypt the message "HELLO WORLD" using the Playfair cipher with the keyword "KEYWORD". The first step is to split the message into pairs of letters:

```
HE LX LO WO RL DX
```

Notice that we added a dummy letter ("X") to the end to make the message even. Now we can encrypt each pair of letters:

```
HE -> RM
LX -> DN
LO -> VO
WO -> HV
RL -> YX
DX -> GU
```

Finally, we combine the encrypted pairs of letters to get the ciphertext:

```
RM DN VO HV YX GU
```

To decrypt a message using the Playfair cipher, the process is simply reversed. The ciphertext is split into pairs of letters, and each pair is decrypted using the same grid. Here is an example of decrypting the above ciphertext:

```
RM -> HE
DN -> LX
VO -> LO
HV -> WO
YX -> RL
GU -> DX
```

Finally, we combine the decrypted pairs of letters to get the original message:

```
HELXLOWORLXDX
```
Notice that we did not include the dummy "X" at the end, since it

## Usage

```python
from playfair import Playfair

# Instantiate a Playfair Cipher object with a key
pf = Playfair("SECRETKEY")

# Print the coder table
pf.print_coder_table()

# Encrypt a message
encrypted_text = pf.encrypt("HELLO WORLD")
print(encrypted_text)

# Decrypt a message
decrypted_text = pf.decrypt(encrypted_text)
print(decrypted_text)
```

## License
MIT