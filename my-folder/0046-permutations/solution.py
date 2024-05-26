class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(res):
            if len(res) == len(nums):
                ans.append(res.copy())
                return
                
            for i in nums:
                if i not in res:
                    res.append(i)
                    backtrack(res)
                    res.pop()
    
        ans = []
        backtrack([])
        return ans
