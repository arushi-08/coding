class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums:
            chosen = [False]*(len(nums)+1)
            curr = []
            self.dfs(nums, res, curr, 0)
        return res
    
    def dfs(self, nums, res, curr, idx):
        res.append(curr)
        
        for i in range(idx, len(nums)):
            self.dfs(nums, res, curr + [nums[i]], i+1)
        
