class PermutationCipher:
    """
    A class that implements a permutation cipher.

    Args:
        key (list): A list of integers representing the permutation to use.

    Attributes:
        key (list): A list of integers representing the permutation to use.
        key_size (int): The length of the key.

    Methods:
        permute(section: str) -> str:
            Permutes the characters in the given section of plaintext.

        inv_permute(section: str) -> str:
            Inverse permutes the characters in the given section of ciphertext.

        encrypt(plaintext: str) -> str:
            Encrypts the given plaintext using the permutation cipher.

        decrypt(cipher_text: str) -> str:
            Decrypts the given ciphertext using the permutation cipher.
    """
    
    def __init__(self, key: list):
        self.key = key
        self.key_size = len(self.key)
    
    def permute(self, section: str) -> str:
        answer = ""
        for key in self.key:
            answer += section[key]
        return answer
    
    def inv_permute(self, section: str) -> str:
        answer = [""] * self.key_size
        for i in range(self.key_size):
            answer[self.key[i]] = section[i]
        return "".join(answer)
    
    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.upper()
        words = plaintext.split()
        plaintext = "".join(words)
        cipher_text = ""
        sections = []
        for i in range(0, len(plaintext), self.key_size):
            sections.append(plaintext[i:i+self.key_size])
        if len(sections[-1]) < self.key_size:
            sections[-1] += 'X' * (self.key_size - len(sections[-1]))
        encrypted_sections = [self.permute(section) for section in sections]
        return "".join(encrypted_sections)
    
    def decrypt(self, cipher_text):
        plaintext = [""] * len(cipher_text)
        sections = []
        for i in range(0, len(cipher_text), self.key_size):
            sections.append(cipher_text[i:i+self.key_size])
        decrypted_sections = [self.inv_permute(section) for section in sections]
        return "".join(decrypted_sections)

