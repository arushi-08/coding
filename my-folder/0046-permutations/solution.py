class Solution:
    def __init__(self):
        self.res = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        chosen = [False] * len(nums)
        res = []
        
        self.backtrack(nums, chosen)
        return self.res
    
    def backtrack(self, nums, chosen, permutations=[]):
            
        if len(permutations) == len(nums):
            self.res.append(permutations.copy())
            return
        for i in range(len(nums)):
            if not chosen[i]:
                permutations.append(nums[i])
                chosen[i] = True
                self.backtrack(nums, chosen, permutations)
                chosen[i] = False
                permutations.remove(nums[i])
        
        
