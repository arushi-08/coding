class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # increase score by nums[i]
        # nums[i] = ceil(nums[i]/3)
        # return max score after k ops

        # nums=[10,10,10,10,10]
        # score = 10, nums=[4,10,10,10,10]
        # score = 20
        # 
        nums = [-i for i in nums]
        heapify(nums)
        score = 0
        while k:
            val = heappop(nums)
            # print(-val, math.ceil(-val/3))
            score += -(val)
            heappush(nums, -math.ceil(-val/3))
            k -= 1
        
        return score

