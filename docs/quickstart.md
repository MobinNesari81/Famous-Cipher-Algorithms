jupyter nbconvert --template "pythoncodeblocks.tpl" --to markdown README.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[<img src='https://github.com/MobinNesari81/Famous-Cipher-Algorithms/tree/main/Logos/FCA-light.svg' width=\"300\">](https://github.com/MobinNesari81/Famous-Cipher-Algorithms)\n",
    "# Quickstart\n",
    "\n",
    "### Tutorial written by <a href=\"https://www.linkedin.com/in/mobin-nesari/\">Mobin Nesari</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this tutorial, we are going to install `FamousCipherAlgorithms` package and use it with some testcases."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"admonition note\">\n",
    "<p class=\"admonition-title\">Note</p>\n",
    "<dl class=\"simple\">\n",
    "<dt>This tutorial is a static non-editable version. Interactive, editable versions are available via the following links:</dt><dd><ul class=\"simple\">\n",
    "<li><p><a class=\"reference external\" href=\"https://colab.research.google.com/github/jeshraghian/snntorch/blob/master/examples/quickstart.ipynb\">Google Colab</a></p></li>\n",
    "<li><p><a class=\"reference external\" href=\"https://github.com/jeshraghian/snntorch/tree/master/examples\">Local Notebook (download via GitHub)</a></p></li>\n",
    "</ul>\n",
    "</dd>\n",
    "</dl>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Install\n",
    "To install `FamousCipherAlgorithms`, you can use this command:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: FamousCipherAlgorithms in /Users/mobinnesari/opt/anaconda3/lib/python3.9/site-packages (0.1.2)\r\n",
      "Requirement already satisfied: numpy<=1.21.5 in /Users/mobinnesari/opt/anaconda3/lib/python3.9/site-packages (from FamousCipherAlgorithms) (1.21.5)\r\n"
     ]
    }
   ],
   "source": [
    "!pip install FamousCipherAlgorithms"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import Package\n",
    "You can import `FamousCipherAlgorithms` in two ways:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1- Import entire package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import FamousCipherAlgorithms as FCA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2- Import specific objects from package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from FamousCipherAlgorithms import Affine, Vigenere, Shift"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Examples\n",
    "Here are a few examples of how package algorithms work. Please feel free to checkout full documentation for each algorithm."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Shift Cipher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " text: Hello World!\n",
      " encrypted: Mjqqt Btwqi!\n",
      " decrypted: Hello World!\n"
     ]
    }
   ],
   "source": [
    "shift = FCA.ShiftCipher(5) # Instantiate a Shift Cipher with K = 5\n",
    "text = \"Hello World!\"\n",
    "enc = shift.encrypt(text)\n",
    "dec = shift.decrypt(enc)\n",
    "print(f\" text: {text}\\n encrypted: {enc}\\n decrypted: {dec}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Affine Cipher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " text: Hello World!\n",
      " encrypted: armmv tvemo!\n",
      " decrypted: hello world!\n"
     ]
    }
   ],
   "source": [
    "affine = FCA.AffineCipher(3, 5) # Instantiate a Affine Cipher with a = 3 and b = 5\n",
    "text = \"Hello World!\"\n",
    "enc = affine.encrypt(text)\n",
    "dec = affine.decrypt(enc)\n",
    "print(f\" text: {text}\\n encrypted: {enc}\\n decrypted: {dec}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Vigenere Cipher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " text: Hello World!\n",
      " encrypted: MEXZI OQZAK!\n",
      " decrypted: HELLO WORLD!\n"
     ]
    }
   ],
   "source": [
    "vigenere = FCA.VigenereCipher(\"FamousCipherAlgorithms\") # Instantiate a Playfair Cipher with key = \"FCA\"\n",
    "text = \"Hello World!\"\n",
    "enc = vigenere.encrypt(text)\n",
    "dec = vigenere.decrypt(enc)\n",
    "print(f\" text: {text}\\n encrypted: {enc}\\n decrypted: {dec}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "That’s it for the quick intro to `FamousCipherAlgorithms`!\n",
    "\n",
    "Please make sure to checkout full document for each cipher algorithm."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
