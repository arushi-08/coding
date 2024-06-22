class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        negative = set()
        maxk = -1
        for i in range(len(nums)):
            if nums[i] < 0:
                negative.add(nums[i])
        
        for i in range(len(nums)):
            if nums[i] > maxk and -nums[i] in negative:
                maxk = nums[i]
        
        return maxk
            
