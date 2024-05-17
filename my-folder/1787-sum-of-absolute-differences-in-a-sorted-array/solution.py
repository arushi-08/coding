class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        psum = []
        cursum = 0
        for num in nums:
            cursum += num
            psum.append(cursum)

        ans = [0] * len(nums)
        total = sum(nums)
        for i in range(len(nums)):
            if i == 0 :
                ans[i] = ((cursum - psum[i]) - nums[i] * (len(nums) - 1 - i))
            else:
                ans[i] = (nums[i] * (i) - psum[i-1]) + ((cursum - psum[i]) - nums[i] * (len(nums) - 1 - i))

        return ans
