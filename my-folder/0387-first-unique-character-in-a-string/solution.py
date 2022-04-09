class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
            
        for key, value in dict1.items():
            if value == 1:
                return s.index(key)
        
        return -1
