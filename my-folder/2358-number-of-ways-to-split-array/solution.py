class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        # valid splits
        # sum of left elems >= sum of right elems
        # atleast 1 elem in right

        psum = [nums[0]]
        for i in range(1, len(nums)):
            psum.append(nums[i] + psum[-1])
        
        # 10,14,6,13
        ans = 0
        for i in range(len(nums)-1):
            leftsum = psum[i]
            rightsum = psum[-1] - leftsum
            if leftsum >= rightsum:
                ans += 1
        
        return ans
