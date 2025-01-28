class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        # given 2 strings s and t
        # s = abcabc, t = abc
        # return largest string x such that x divides both s and t

        # 

        if len(str1) > len(str2):
            str1, str2 = str2, str1

        
        def can_divide(t):
            if not t: return False
            return t * (len(str1)//len(t)) == str1 and t * (len(str2)//len(t)) == str2
        
        for i in range(len(str1)-1,-1,-1):
            if can_divide(str1[:i+1]):
                return str1[:i+1]
        
        return ''



