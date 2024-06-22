class Solution:
    def maxDepth(self, s: str) -> int:
        

        depth = 0
        maxdepth = depth
        for i in s:
            if i == '(':
                depth += 1
            elif i == ')':
                depth -= 1
            maxdepth = max(maxdepth, depth)
        
        return maxdepth
            

