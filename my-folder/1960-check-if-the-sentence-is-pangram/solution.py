class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        

        alphabet = [0] * 26
        for i in range(len(sentence)):
            alphabet[ord(sentence[i]) - ord('a')] += 1
        
        for i in range(len(alphabet)):
            if alphabet[i] == 0:
                return False
        
        return True
