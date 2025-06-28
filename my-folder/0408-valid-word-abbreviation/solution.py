class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        wi = 0
        aj = 0
        while wi < len(word) and aj < len(abbr):

            if abbr[aj].isalpha():
                if abbr[aj] != word[wi]:
                    return False

                wi += 1
                aj += 1
            else:
                if abbr[aj] == '0':
                    return False
                
                num = 0

                while aj < len(abbr) and abbr[aj].isdigit():
                    num = num * 10 + (ord(abbr[aj]) - ord('0'))
                    aj += 1
                
                wi += num
        
        return aj == len(abbr) and wi == len(word)
