class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        
        count, left = 1,0

        for right in range(1, len(nums)):
            if nums[right] == nums[right-1]:
                left = right
            count += right - left + 1
        
        return count

        
