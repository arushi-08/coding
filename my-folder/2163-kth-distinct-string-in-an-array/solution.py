class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        hmap = {}
        unique_strings = []
        for string in arr:
            hmap[string] = hmap.get(string, 0) + 1
            if hmap[string] == 1:
                unique_strings.append(string)
        
        for string in unique_strings:
            if hmap[string] == 1:
                k -= 1
            if k == 0:
                return string
        
        return ""
