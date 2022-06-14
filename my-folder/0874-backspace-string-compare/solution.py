class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s = self.backspace_char(s)
        t = self.backspace_char(t)
        
        return s == t
        
    
    def backspace_char(self, s):
        i = 0
        while i < len(s):
            if s[i] == "#":
                print(s[:i-1], s[i+1:])
                if i-1 >= 0:
                    
                    s = list(s[:i-1]+s[i+1:])
                    i -= 1
                else:
#                     i == 0
                    s = list(s[i+1:])
            else:
                s = list(s)
                i += 1
        print("ans", s)
        return s
        
