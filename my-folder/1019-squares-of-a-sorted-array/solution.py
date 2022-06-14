class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] *= nums[i]
            
        i = 0
        j = len(nums) - 1
        result = [None]*len(nums)
        start = 0
        end = len(result) - 1
        while (i <= j):
            if nums[i] < nums[j]:
                result[end] = nums[j]
                j -= 1
                end -= 1
            else:
                result[end] = nums[i]
                i += 1
                end -= 1
        
        return result
                
        
            
            
