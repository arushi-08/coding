from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        f_map = Counter(arr)
        if len(f_map.values()) == len(set(f_map.values())):
            return True
        return False
