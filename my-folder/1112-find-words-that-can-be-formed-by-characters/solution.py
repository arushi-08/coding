class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        ans = 0
        cmap = Counter(chars)
        for w in words:
            include = True
            temp = cmap.copy() 
            for char in w:
                if char in temp:
                    temp[char] -= 1
                    if temp[char]==0:
                        del temp[char]
                else:
                    include = False
            if include: 
                ans += len(w)
        
        return ans
