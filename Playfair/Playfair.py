
class Playfair:
    """
    Initializes a Playfair cipher object with the given key.

    :param key: A string representing the key to use for the cipher.
    :type key: str
    :raises Exception: If the key contains duplicate characters or both "i" and "j".
    """
    def __init__(self, key: str) -> None:
        self.key = key.lower()
        self.alphabets = list("abcdefghklmnopqrstuvwxyz".strip())
        self.alphabets.insert(8,"i/j")
        if len(set(list(self.key.strip()))) != len(self.key):
            raise Exception("Key should contains unique values")
        if 'i' in self.key and 'j' in self.key:
            raise Exception("Key shouldn't contain i and j at the same time")
        self.coder_table = [['' for _ in range(5)] for _ in range(5)]
        i_idx = 0
        j_idx = 0
        for char in self.key:
            if char == 'i' or char == 'j':
                char = 'i/j'
            if j_idx == 5:
                j_idx = 0
                i_idx += 1
            self.coder_table[i_idx][j_idx] = char
            j_idx += 1
        
        for char in self.alphabets:
            if char not in self.key:
                if char == 'i/j':
                    if 'i' not in self.key and 'j' not in self.key:
                        self.coder_table[i_idx][j_idx] = char
                        j_idx += 1
                else:
                    self.coder_table[i_idx][j_idx] = char
                    j_idx += 1
            if j_idx == 5:
                j_idx = 0
                i_idx += 1

    def print_coder_table(self) -> None:
        """
        Prints the coder table to the console.
        """
        for i in range (5):
            for j in range (5):
                print(self.coder_table[i][j] + '  ', end='')
            print("\n")
        print(end='\n')
    
    def msg_parser(self, msg: str) -> list:
        """
        Splits the message into bigrams.

        :param msg: A string representing the message to split.
        :type msg: str
        :return: A list of bigrams.
        :rtype: list
        """
        answer = []
        i = 0
        while i < len(msg) - 1:
            if msg[i] != msg[i + 1]:
                answer.append(msg[i] + msg[i+1])
                i += 2
            else:
                answer.append(msg[i] + 'x')
                i += 1
        if i == len(msg) - 1:
            answer.append(msg[i] + 'x')
        print("parser result:", answer)
        return answer
    
    def get_next_chars(self, chars: str) -> str:
        """
        Returns the cipher text of the given bigram.

        :param chars: A string representing the bigram to cipher.
        :type chars: str
        :return: A string representing the cipher text of the given bigram.
        :rtype: str
        """
        answer = ""
        c1 = chars[0]
        c2 = chars[1]
        if c1 == 'i' or c1 =='j':
            c1 = 'i/j'
        if c2 == 'i' or c2 =='j':
            c2 = 'i/j'
        p1 = (0,0)
        p2 = (0,0)
        for i in range(5):
            for j in range(5):
                if c1 == self.coder_table[i][j]:
                    p1 = (i, j)
                
                elif c2 == self.coder_table[i][j]:
                    p2 = (i, j)
        
        if p1[0] == p2[0]:
            # Same row
            answer += self.coder_table[p1[0]][(p1[1] + 1) % 5]
            answer += self.coder_table[p2[0]][(p2[1] + 1) % 5]
        
        elif p1[1] == p2[1]:
            # Same column
            answer += self.coder_table[(p1[0] + 1) % 5][p1[1]]
            answer += self.coder_table[(p2[0] + 1) % 5][p2[1]]
        
        else:
            # Square format
            answer += self.coder_table[p1[0]][p2[1]]
            answer += self.coder_table[p2[0]][p1[1]]
        
        if 'i/j' in answer:
            answer = answer.replace('i/j', 'i')
        return answer
    
    def get_prev_chars(self, chars: str) -> str:
        """
        Returns the plain text of the given bigram.

        :param chars: A string representing the bigram to plaintext.
        :type chars: str
        :return: A string representing the plain text of the given bigram.
        :rtype: str
        """
        answer = ""
        c1 = chars[0]
        c2 = chars[1]
        if c1 == 'i' or c1 =='j':
            c1 = 'i/j'
        if c2 == 'i' or c2 =='j':
            c2 = 'i/j'
        p1 = (0,0)
        p2 = (0,0)
        for i in range(5):
            for j in range(5):
                if c1 == self.coder_table[i][j]:
                    p1 = (i, j)
                
                elif c2 == self.coder_table[i][j]:
                    p2 = (i, j)
        
        if p1[0] == p2[0]:
            # Same row
            answer += self.coder_table[p1[0]][(p1[1] - 1) % 5]
            answer += self.coder_table[p2[0]][(p2[1] - 1) % 5]
        
        elif p1[1] == p2[1]:
            # Same column
            answer += self.coder_table[(p1[0] - 1) % 5][p1[1]]
            answer += self.coder_table[(p2[0] - 1) % 5][p2[1]]
        
        else:
            # Square format
            answer += self.coder_table[p1[0]][p2[1]]
            answer += self.coder_table[p2[0]][p1[1]]
        
        if 'i/j' in answer:
            answer = answer.replace('i/j', 'i')
        
        return answer
    
    def encrypt(self, msg: str) -> str:
        """
        Takes a string message and encrypts it using the Playfair cipher.
        
        Arguments:
        message -- a string message to be encrypted
        
        Returns:
        A string representing the encrypted message.
        """
        answer = ""
        msg = msg.lower()
        msg = msg.replace(' ', '')
        msg_parsed = self.msg_parser(msg)
        for section in msg_parsed:
            answer += self.get_next_chars(section)
        return answer
    
    def decrypt(self, msg: str) -> str:
        """
        Takes a string message and decrypts it using the Playfair cipher.
        
        Arguments:
        message -- a string message to be decrypted
        
        Returns:
        A string representing the decrypted message.
        """
        answer = ""
        msg = msg.lower()
        msg_parsed = self.msg_parser(msg)
        for section in msg_parsed:
            answer += self.get_prev_chars(section)
        return answer
