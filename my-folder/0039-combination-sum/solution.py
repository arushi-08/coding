class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(index, path, pathsum):
            if pathsum > target: return
            if pathsum == target:
                res.append(path.copy())
                return
            
            for i in range(index, len(candidates)):
                if pathsum+candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(i, path, pathsum+candidates[i])
                    path.pop()
                
        
        backtrack(0, [], 0)
        return res
