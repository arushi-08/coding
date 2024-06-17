class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cursum = sum(nums[:k])
        st = 0
        ed = k
        maxsum = cursum
        while st < len(nums)-k:
            cursum += - nums[st] + nums[ed]
            maxsum = max(maxsum, cursum)
            st += 1
            ed += 1
        return maxsum / k

