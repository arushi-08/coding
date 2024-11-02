class Solution:
    def makeFancyString(self, s: str) -> str:
        
        curr_char = ''
        count = 0
        new_s = []
        for i in range(len(s)):
            if s[i] == curr_char:
                count += 1
            else:
                curr_char = s[i]
                count = 1
            
            if count < 3:
                new_s.append(s[i])
        
        return ''.join(new_s)
        
