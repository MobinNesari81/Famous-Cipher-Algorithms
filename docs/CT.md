<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>

# Columnar Transposition Cipher

Columnar Transposition Cipher is a type of transposition cipher in which the plaintext is rearranged and then encrypted. In this technique, the plaintext is written in rows and then read out column by column. The order of the columns is determined by a keyword or a key phrase provided by the sender.

## How It Works

1. Choose a keyword or a key phrase. For example, "SECRET" or "TOP SECRET".
2. Write down the plaintext in rows under the keyword/keyphrase.
    ```
    Keyword: SECRET
    Plaintext: ATTACKATDAWN

    S E C R E T
    A T T A C K
    A T D A W N
    ```

3. Reorder the columns based on the alphabetical order of the letters in the keyword/keyphrase.
    ```
    Keyword: SECRET
    Reordered columns: C E R S T
    Plaintext: ATAATTKCDKANW

    C E R S T
    A T T A C K
    A T D A W N
    ATAATTKCDKANW
    ```

The ciphertext is obtained by reading out the reordered columns row by row.
```
Ciphertext: ATAATTKCDKANW
```

## Strengths and Weaknesses
One of the strengths of Columnar Transposition Cipher is that it is relatively easy to understand and implement. It can be used to quickly encrypt messages and, when combined with other encryption techniques, can provide a basic level of security. However, one of its weaknesses is that it is vulnerable to frequency analysis attack, where an attacker can use statistical methods to analyze the frequency of letters in the ciphertext and deduce the original plaintext. Additionally, it does not provide any form of message authentication, which means it is susceptible to message tampering or forgery. Overall, while Columnar Transposition Cipher can be useful in certain contexts, it should not be relied upon as the sole method of encryption for sensitive information.

## Usage
The `ColumnarTranspositionCipher` class in this module can be used to encrypt and decrypt messages using the Columnar Transposition Cipher. To use it, simply create a new instance of the class with a key, and then call the `encrypt()` or `decrypt()` method with the plaintext or ciphertext respectively.

```python
import FamousCipherAlgorithms as FCA
CTC = FCA.ColumnarTranspositionCipher("3142")
text = "I WILL SEE YOU TONIGHT"
ciphertext = CTC.encrypt(text)
decrypted = CTC.decrypt(ciphertext)

print(f" Text: {text}\n Ciphertext: {ciphertext}\n Decrypted Text: {decrypted}")
```

The result will be:

```
 Text: I WILL SEE YOU TONIGHT
 Ciphertext: WSONTLETGXILYOHIEUIX
 Decrypted Text: IWILLSEEYOUTONIGHT
```

## References
<a href="https://en.wikipedia.org/wiki/Transposition_cipher#:~:text=In%20a%20columnar%20transposition%2C%20the,usually%20defined%20by%20a%20keyword.">Wikipedia: Transposition Cipher</a>
