class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums: return []
        i = 0
        ans = []
        while i < len(nums):
            st = i
            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if st != i:
                ans.append(f"{nums[st]}->{nums[i]}")
            else:
                ans.append(str(nums[i]))
            i += 1

        return ans
