class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        esum = sum(nums)
        dsum = 0
        for n in nums:
            while n:
                n, remain = divmod(n, 10)
                dsum += remain
        return abs(dsum - esum)

