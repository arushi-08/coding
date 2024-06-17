class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []
        for i in range(len(nums)):
            if lower < nums[i]:
                ans.append([lower, nums[i]-1])
            
            lower = nums[i] + 1

        if lower <= upper:
            ans.append([lower, upper])
        
        return ans

