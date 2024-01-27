class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        dup = set()
        ans = set()
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
                hmap = {}
                for j in range(i+1, len(nums)):
                    if nums[j] in hmap:
                        if nums[j] + hmap[nums[j]] + nums[i] == 0:
                            ans.add(tuple(sorted([nums[j], hmap[nums[j]], nums[i]])))               
                            
                    else:
                        hmap[-nums[i] - nums[j]] = nums[j]
        
        return ans

                        
