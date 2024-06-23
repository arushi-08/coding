class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        posi = 0
        negi = 1
        
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            if nums[i] > 0:
                ans[posi] = nums[i]
                posi += 2
            else:
                ans[negi] = nums[i]
                negi += 2
        
        return ans
