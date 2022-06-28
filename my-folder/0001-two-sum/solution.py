class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for i, val in enumerate(nums):
            print(i, val)
            remaining = target - val
            
            if remaining in hmap:
                return [hmap[remaining], i]
            
            hmap[val] = i
        
        print(hmap)
