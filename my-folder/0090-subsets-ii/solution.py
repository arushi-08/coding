class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if nums:
            self.dfs(sorted(nums), res, [], 0)
        return res
    
    def dfs(self, nums, res, curr, idx):
        if curr not in res:
            res.append(curr)
        
        for i in range(idx, len(nums)):
            self.dfs(nums, res, curr + [nums[i]], i+1)
