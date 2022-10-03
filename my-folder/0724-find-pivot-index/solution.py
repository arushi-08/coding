class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
#         sum of nums to left = sum of nums to right -> return index
        if not nums:
            return -1
        pref_sum = [nums[0]]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            pref_sum.append(pref_sum[-1]+num)
        
        for i, num in enumerate(nums):
            if pref_sum[i]-nums[i] == pref_sum[-1] - pref_sum[i]:
                return i
        
        return -1
