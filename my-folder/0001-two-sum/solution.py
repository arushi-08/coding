class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        summap = {}
        
        for i, num in enumerate(nums):
            if num in summap:
                return  [summap[num], i]
            
            summap[target - num] = i
        

        
