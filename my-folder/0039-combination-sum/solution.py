class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        if target:
            self.helper(candidates, target, res, curr)
            # res = list(set(tuple(sorted(sub)) for sub in res))
        return res
    
    def helper(self, candidates, target, res, curr):
        
        if target == 0:
            res.append(curr.copy())
            return 
        
        if target < 0: return
        
        for i in range(len(candidates)):
            curr.append(candidates[i])
            self.helper(candidates[i:], target - candidates[i], res, curr)
            curr.pop()
        
