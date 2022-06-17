class Solution:
    
    def __init__(self):
        self.memo = {}
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle : return 0
        if len(triangle) == 1 : return triangle[0][0]
        
        return self.helper(triangle, 0, 0)
    
    def helper(self, triangle, idx, root):
        
        if len(triangle) == idx: return 0
        
        if (idx, root) in self.memo:
            return self.memo[(idx, root)]
        
        if len(triangle[idx]) > root + 1:
            self.memo[(idx, root)] = min(self.helper(triangle, idx+1, root) + triangle[idx][root], 
                       self.helper(triangle, idx+1, root + 1) + triangle[idx][root + 1])
        
        else: self.memo[(idx, root)] = self.helper(triangle, idx+1, root) + triangle[idx][root]
        
        return self.memo[(idx, root)]
