class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        # # of pairs with diff == k

        hmap = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] - k in hmap:
                count += hmap[nums[i] - k]
            if nums[i] + k in hmap:
                count += hmap[nums[i] + k]
            hmap[nums[i]] = hmap.get(nums[i], 0) + 1
        return count

