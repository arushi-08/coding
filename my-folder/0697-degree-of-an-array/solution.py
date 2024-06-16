class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
    
        left, right, count = {}, {}, {}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        ans = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
            
        return ans
