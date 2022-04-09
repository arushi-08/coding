class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        
        
        for j in t:
            if j in dict1.keys() and dict1[j] > 0:
                dict1[j] -= 1
                if dict1[j] == 0:
                    dict1.pop(j)
                
            else:
                return False
        
        if dict1:
            return False
        
        return True
