class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        # count num of subarr, nums[i-1] + nums[i+1] == nums[i]//2
        result = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] + nums[i+1] == nums[i]/2 :
                result += 1
        
        return result
