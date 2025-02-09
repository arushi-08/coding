class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        #  a pair of indices (i,j) -> bad pair
        # i < j and j - i != nums[j] - nums[i]
        # calculate total - good pairs
        # total = n*(n-1)/2
        # good => nums[i] - i == nums[j] - j
        # 1,3,2,4
        # 0,2,0,0

        hmap = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            hmap[num-i] = hmap.get(num-i, 0) + 1
        
        for k in hmap:
            if hmap[k] > 1:
                good_pairs += hmap[k] * (hmap[k]-1)//2
        
        n = len(nums)
        
        return n*(n-1)//2 - good_pairs

