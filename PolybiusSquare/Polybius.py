class PolybiusSquareCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.square = [["A", "B", "C", "D", "E"],
                       ["F", "G", "H", "I", "K"],
                       ["L", "M", "N", "O", "P"],
                       ["Q", "R", "S", "T", "U"],
                       ["V", "W", "X", "Y", "Z"]]
    
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext.upper():
            if char == "J":
                char = "I"
            if char in self.alphabet:
                row, col = self.find_char(char)
                ciphertext += str(row) + str(col)
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        i = 0
        while i < len(ciphertext):
            row = int(ciphertext[i])
            col = int(ciphertext[i+1])
            plaintext += self.square[row-1][col-1]
            i += 2
        return plaintext
    
    def find_char(self, char):
        for i in range(len(self.square)):
            for j in range(len(self.square[i])):
                if self.square[i][j] == char:
                    return i+1, j+1


if __name__ == "__main__":
    PSC = PolybiusSquareCipher()
    text = "I will see you at midnight"
    enc = PSC.encrypt(text)
    print(enc)
    dec = PSC.decrypt(enc)
    print(f" Text: {text}\n Ciphertext: {enc}\n Decrypted: {dec}")