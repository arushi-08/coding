class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        hmap = {}
        maxsum = 0
        for num in nums:
            digitsum = 0
            numdup = num
            while numdup:
                digitsum += numdup%10
                numdup //= 10
            
            if digitsum in hmap:
                maxsum = max(maxsum, hmap[digitsum] + num)
                hmap[digitsum] = max(hmap[digitsum], num)
            else:
                hmap[digitsum] = num
        
        if maxsum == 0:
            return -1
        return maxsum

        
        
            
