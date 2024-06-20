class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        st = 0
        i = 0
        while i < len(abbr):
            if st >= len(word):
                return False

            if abbr[i].isalpha() and abbr[i] != word[st]:
                return False
            
            if abbr[i].isdigit():
                j = i
                if abbr[j] == "0": # leading zeros -> not valid abbrv return False
                    return False

                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                
                abbr_count = int(abbr[j:i]) + st
                while st < len(word): # iterate on word till abbrv count
                    st += 1
                    if st == abbr_count:
                        break
                        
                if st == len(word) and st < abbr_count:
                    return False
            else:
                i += 1
                st += 1
            
        return st == len(word)


            
