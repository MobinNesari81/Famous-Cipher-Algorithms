# Quickstart

###### Tutorial written by <a href="https://www.linkedin.com/in/mobin-nesari/">Mobin Nesari</a>

In this tutorial, we are going to install `FamousCipherAlgorithms` package and use it with some testcases.

<div class="admonition note">
<p class="admonition-title">Note</p>
<dl class="simple">
<dt>This tutorial is a static non-editable version. Interactive, editable versions are available via the following links:</dt><dd><ul class="simple">
<li><p><a class="reference external" href="https://colab.research.google.com/github/jeshraghian/snntorch/blob/master/examples/quickstart.ipynb">Google Colab</a></p></li>
<li><p><a class="reference external" href="https://github.com/jeshraghian/snntorch/tree/master/examples">Local Notebook (download via GitHub)</a></p></li>
</ul>
</dd>
</dl>
</div>

## Install
To install `FamousCipherAlgorithms`, you can use this command:


```python
!pip install FamousCipherAlgorithms
```

    Requirement already satisfied: FamousCipherAlgorithms in /Users/mobinnesari/opt/anaconda3/lib/python3.9/site-packages (0.1.2)
    Requirement already satisfied: numpy<=1.21.5 in /Users/mobinnesari/opt/anaconda3/lib/python3.9/site-packages (from FamousCipherAlgorithms) (1.21.5)


## Import Package
You can import `FamousCipherAlgorithms` in two ways:

1- Import entire package


```python
import FamousCipherAlgorithms as FCA
```

2- Import specific objects from package


```python
from FamousCipherAlgorithms import Affine, Vigenere, Shift
```

## Examples
Here are a few examples of how package algorithms work. Please feel free to checkout full documentation for each algorithm.

### Shift Cipher


```python
shift = FCA.ShiftCipher(5) # Instantiate a Shift Cipher with K = 5
text = "Hello World!"
enc = shift.encrypt(text)
dec = shift.decrypt(enc)
print(f" text: {text}\n encrypted: {enc}\n decrypted: {dec}")
```

     text: Hello World!
     encrypted: Mjqqt Btwqi!
     decrypted: Hello World!


### Affine Cipher


```python
affine = FCA.AffineCipher(3, 5) # Instantiate a Affine Cipher with a = 3 and b = 5
text = "Hello World!"
enc = affine.encrypt(text)
dec = affine.decrypt(enc)
print(f" text: {text}\n encrypted: {enc}\n decrypted: {dec}")
```

     text: Hello World!
     encrypted: armmv tvemo!
     decrypted: hello world!


### Vigenere Cipher


```python
vigenere = FCA.VigenereCipher("FamousCipherAlgorithms") # Instantiate a Playfair Cipher with key = "FCA"
text = "Hello World!"
enc = vigenere.encrypt(text)
dec = vigenere.decrypt(enc)
print(f" text: {text}\n encrypted: {enc}\n decrypted: {dec}")
```

     text: Hello World!
     encrypted: MEXZI OQZAK!
     decrypted: HELLO WORLD!


## Conclusion

That’s it for the quick intro to `FamousCipherAlgorithms`!

Please make sure to checkout full document for each cipher algorithm.


