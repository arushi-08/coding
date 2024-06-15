class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        change = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                change += 1
        
        return change
