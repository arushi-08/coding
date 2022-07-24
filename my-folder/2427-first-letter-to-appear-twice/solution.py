class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
            if s_dict[i] >= 2:
                return i
