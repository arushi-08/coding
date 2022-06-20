class Solution:
    # def __init__(self):
        # self.res = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        chosen = [False] * len(nums)
        res = []
        self.dfs(nums, [], chosen, res)
        return res
    
    def dfs(self, nums, curr_permutation, chosen, res):
        
        if len(curr_permutation) == len(nums):
            res.append(curr_permutation.copy())
            return
        
        for i in range(len(nums)):
            if not chosen[i]:
                curr_permutation.append(nums[i])
                chosen[i] = True

                self.dfs(nums, curr_permutation, chosen, res)

                curr_permutation.remove(nums[i])
                chosen[i] = False
            
        
