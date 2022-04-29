from itertools import chain
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}
        
        for i in strs:
            key = tuple(sorted(i))
            dict1[key] = dict1.get(key, []) + [i]
        
        return list(dict1.values())
