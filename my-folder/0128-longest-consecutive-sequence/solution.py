class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums.sort()

        currans = 0
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                currans += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                ans = max(currans+1, ans)
                currans = 0
        
        return max(ans, currans+1)
