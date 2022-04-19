class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum_n = sum(nums)
        actual_sum = int((len(nums)*(len(nums)+1))/2)
        return actual_sum - sum_n
        
            
