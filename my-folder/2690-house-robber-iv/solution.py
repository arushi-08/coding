class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        start = min(nums)
        end = max(nums)
        res = end
        while start <= end:
            mid = (start + end) // 2
            print('mid', mid)
            if self.check_current(mid, nums, k):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return res

    def check_current(self, mid, nums, k):

        count_lt_mid = 0
        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                count_lt_mid += 1
                i += 2
            else:
                i += 1
            if count_lt_mid == k:
                return True
        
        return count_lt_mid == k
        

